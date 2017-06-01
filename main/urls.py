from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^create_coffee/$', views.create_coffee, name='create_coffee'),
    url(r'^edit_coffee/(?P<coffee_id>[0-9]+)/$', views.edit_coffee, name="edit_coffee"),
]
