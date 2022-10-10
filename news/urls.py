from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/<int:pk>', views.new_detail, name='new_detail'),
    path('', views.NewListView.as_view(), name='news_list'),
    path('tag/<slug:slug>', views.NewListView.as_view(), name='new_list_by_tag'),
    path('analytics', views.AnaliticsListView.as_view(), name='analytics')
    ]
