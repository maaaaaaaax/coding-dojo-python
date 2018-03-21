from django.conf.urls import url, include
from . import views           # From the current directoy, import views.py
urlpatterns = [
    url(r'^$', views.index), # Any request should be handled by the views.py's index method
    url(r'^checkout', views.checkout),
    url(r'^review', views.review),
    url(r'^reset$', views.reset),
]
