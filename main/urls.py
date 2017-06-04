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

    url(r'^create_roast/$', views.create_roast, name='create_roast'),
    url(r'^edit_roast/(?P<roast_id>[0-9]+)/$', views.edit_roast, name="edit_roast"),
    url(r'^delete_roast/(?P<roast_id>[0-9]+)/$', views.delete_roast, name="delete_roast"),

    url(r'^create_powder/$', views.create_powder, name='create_powder'),
    url(r'^edit_powder/(?P<powder_id>[0-9]+)/$', views.edit_powder, name="edit_powder"),
    url(r'^delete_powder/(?P<powder_id>[0-9]+)/$', views.delete_powder, name="delete_powder"),

    url(r'^create_syrup/$', views.create_syrup, name='create_syrup'),
    url(r'^edit_syrup/(?P<syrup_id>[0-9]+)/$', views.edit_syrup, name="edit_syrup"),
    url(r'^delete_syrup/(?P<syrup_id>[0-9]+)/$', views.delete_syrup, name="delete_syrup"),

    url(r'^create_order/(?P<coffee_id>[0-9]+)/$', views.create_order, name="create_order"),
]
