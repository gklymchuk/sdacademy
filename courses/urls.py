from courses import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<crs_id>\d+)/', views.detail, name="detail"),
)