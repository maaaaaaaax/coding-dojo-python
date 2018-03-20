from django.conf.urls import url
from . import views           # From the current directoy, import views.py
urlpatterns = [
    url(r'^$', views.index), # Any request should be handled by the views.py's index method
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show), # named groups in Python
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),
]


# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /.
