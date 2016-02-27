from coaches import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(?P<c_id>\d+)/', views.detail, name="detail"),
)
