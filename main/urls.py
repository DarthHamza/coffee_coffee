from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),

    url(r'^create_coffee/$', views.create_coffee, name='create_coffee'),
    url(r'^edit_coffee/(?P<coffee_id>[0-9]+)/$', views.edit_coffee, name="edit_coffee"),
    url(r'^delete_coffee/(?P<coffee_id>[0-9]+)/$', views.delete_coffee, name="delete_coffee"),

    url(r'^create_bean/$', views.create_bean, name='create_bean'),
    url(r'^edit_bean/(?P<bean_id>[0-9]+)/$', views.edit_bean, name="edit_bean"),
    url(r'^delete_bean/(?P<bean_id>[0-9]+)/$', views.delete_bean, name="delete_bean"),
]
