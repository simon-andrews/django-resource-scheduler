from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resources/$', views.allresources, name='resources_main'),
    url(r'^resources/(?P<resource_pk>\d*)$', views.specificresource, name='resource'),
    url(r'^resources/new$', views.newresource, name='new_resource'),
    url(r'^reservations/$', views.allreservations, name='reservations_main'),
    url(r'^reservations/(?P<reservation_pk>\d*)$', views.specificreservation, name='reservation'),
    url(r'^reservations/new$', views.newreservation, name='new_reservation'),
]
