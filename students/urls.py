from students import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<st_id>\d+)/', views.detail, name="detail"),
    url(r'^', views.list_view, name="list_view"),
)
