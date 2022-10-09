from .models import New
from .serializers import NewSerializer
from .pagination import VievSetPagination
from rest_framework import viewsets
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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

    def get_queryset(self, **kwargs):

        object_list = New.objects.all()
        
        if self.kwargs.get('tag'):
            tag = get_object_or_404(Tag, slug=self.kwargs['tag'])
        
        return object_list
        

class NewDetailView(DetailView):
    model = New
    template_name = 'new/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'new'
