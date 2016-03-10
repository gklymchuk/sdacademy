from courses import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/add_lesson$', views.add_lesson, name="add-lesson"),
    url(r'^(?P<pk>\d+)/$', views.detail, name="detail"),
    url(r'^edit/(?P<pk>\d+)/', views.edit, name="edit"),
    url(r'^remove/(?P<pk>\d+)/', views.remove, name="remove"),
    url(r'^add/', views.create, name="add"),
)
