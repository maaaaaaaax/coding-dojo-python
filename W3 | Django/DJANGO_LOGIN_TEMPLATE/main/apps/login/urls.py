from django.conf.urls import url
from . import views           # From the current directoy, import views.py
urlpatterns = [
    url(r'^$', views.index), # Any request should be handled by the views.py's index method
    url(r'^sign_up', views.sign_up),
    url(r'^sign_in', views.sign_in),    
    url(r'^success', views.success),
    url(r'^logout', views.logout),
    # url(r'^new', views.add),
    # url(r'^submit_add', views.submit_add),
    # url(r'^(?P<id>\d+)/?$', views.show), # question mark means the question mark may or may not be there
    # url(r'^(?P<id>\d+)/?/edit$', views.edit),
    # url(r'^(?P<id>\d+)/submit_edit/?$', views.submit_edit),
    # url(r'^(?P<id>\d+)/submit_delete/?$', views.submit_delete),
    # url(r'^result', views.result),
    # url(r'^new$', views.reset), #r'^(?P<id>\d+)$
]
