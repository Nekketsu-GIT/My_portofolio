from django.conf.urls import url
from django.urls import path,re_path

from . import views

urlpatterns = [
    path("", views.home, name='blog'),
    re_path(r'^page/(?P<page>\d+)$', views.home, name='archive'),
    path('<slug:slug>', views.post, name='blog_post'),
    #path('authors/', views.authors, name='blog_authors')
]