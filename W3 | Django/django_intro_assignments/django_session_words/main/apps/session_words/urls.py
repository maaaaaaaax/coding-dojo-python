from django.conf.urls import url, include
from . import views           # From the current directoy, import views.py
urlpatterns = [
	url(r'^$', views.index),
	url(r'^submit', views.submit),
	url(r'^reset$', views.reset)
]
