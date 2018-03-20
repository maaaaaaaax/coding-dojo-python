from django.conf.urls import url
from . import views           # From the current directoy, import views.py
urlpatterns = [
    url(r'^$', views.index), # Any request should be handled by the views.py's index method
    url(r'^time_display', views.index),
]
