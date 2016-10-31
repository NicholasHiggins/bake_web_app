from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'bake/(?P<bake_id>[0-9]+)/view/', views.view_bake, name = 'view_bake'),
]
