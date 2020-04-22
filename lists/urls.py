from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(?P<pk>\d+)/$', views.ViewAndAddToList.as_view(), name='view_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
