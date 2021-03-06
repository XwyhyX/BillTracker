
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^pay(/(?P<filterString>\w+)/)?$', views.pay, name = "pay"),
	url(r'^history(/(?P<filterString>\w+)/)?$', views.history, name = "history"),
	url(r'^details/(?P<bill_id>[0-9]+)/$', views.details, name='details')
    
]
