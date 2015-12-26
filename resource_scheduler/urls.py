from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.allresources, name='resources_main'),
    url(r'^resources/(?P<resource_pk>\d*)$', views.specificresource, name='resource'),
]
