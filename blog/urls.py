from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog'),
    url(r'^page/(?P<page>\d+)$', views.home, name='archive'),
    url(r'^(?P<slug>.*)$', views.post, name='blog_post'),
    # url(r'^(?P<slug>.*)$', views.author, name='blog_author'),
    # url(r'^(?P<slug>.*)$', views.category, name='blog_category'),
]