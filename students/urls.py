from students import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<st_id>\d+)/', views.detail, name="detail"),
    url(r'^edit/(?P<pk>\d+)/', views.edit, name="edit"),
    url(r'^add/', views.create, name="add"),
    url(r'^$', views.list_view, name="list_view"),
)
