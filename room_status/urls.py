from django.urls import path
from django.conf.urls import include, url


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    url('update_status', views.update_status, name='update_status'),
    url('toggle', views.toggle, name='toggle'),

]

