from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<author_id>\d+)/(?P<author_slug>[-\w]+)/$', views.author_detail, name="author_detail"),
]
