from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^dashboard$', views.success, name='success'),
    url(r'^logout$',views.logout, name='logout'),
    url(r'^home$', views.success, name='success'),
    url(r'^additemlist$', views.success, name='additemlist'),

]
