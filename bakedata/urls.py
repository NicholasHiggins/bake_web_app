from django.conf.urls import url

from bakedata import views

urlpattern = [
	url(r'^$', views.index, name='index'),
]
