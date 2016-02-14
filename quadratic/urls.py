from quadratic import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^results/', views.quadratic_results, name="results"),
)