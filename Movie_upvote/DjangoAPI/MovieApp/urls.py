from django.conf.urls import url
from MovieApp import views

urlpatterns = [
    url(r'^movie/$', views.MovieApi),
    url(r'^movie/([0-9]+)$', views.MovieApi)
]