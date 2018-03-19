from django.conf.urls import url
from . import views      # From the current directoy, import views.py
urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test),   # Any request should be handled by the views.py's index method
]
