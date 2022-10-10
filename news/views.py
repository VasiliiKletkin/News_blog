from .models import New, Ip
from django.shortcuts import render
from .serializers import NewSerializer
from .pagination import VievSetPagination
from rest_framework import viewsets
from django.views.generic.list import ListView
from taggit.models import Tag
from django.shortcuts import get_object_or_404


class NewViewSet(viewsets.ModelViewSet):
    """
    API News CRUD
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer
    ordering = ['-publish']
    pagination_class = VievSetPagination


class NewListView(ListView):
    model = New
    template_name = 'new/list.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        object_list = New.objects.all()
        if self.kwargs.get('slug'):
            tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
            object_list = object_list.filter(tags__name__in=[tag])
        return object_list


class AnaliticsListView(ListView):
    model = New
    template_name = 'new/analytics.html'
    context_object_name = 'news'
    paginate_by = 10

# Метод для получения айпи


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # В REMOTE_ADDR значение айпи пользователя
        ip = request.META.get('REMOTE_ADDR')
    return ip


def new_detail(request, pk):
    new = get_object_or_404(New, id=pk)
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        new.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        new.views.add(Ip.objects.get(ip=ip))

    context = {
        'new': new,
    }
    return render(request, 'new/detail.html', context)
