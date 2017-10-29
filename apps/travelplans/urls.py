from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^additem$', views.index , name='additem'),
    url(r'^logout$',  views.logout,  name='logout'),
    url(r'^success$', views.home , name='success'),
    url(r'^planlistadd$', views.planlistadd, name='planlistadd'),
    url(r'^planshow/(?P<id>\d+)$', views.itemshow, name='planshow'),
    # url(r'^removeplan/(?P<id>\d+)$', views.removeplan, name='removeplan'),

    # url(r'^showplan/(?P<id>\d+)$', views.planlistadd, name='planlistadd'),
]
