from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.verse_list, name="verse_list"),
    url(r'^(?P<author_slug>[-\w]+)/$', views.verse_list, name="verse_list_by_author"),
    url(r'^(?P<verse_id>\d+)/(?P<verse_slug>[-\w]+)/$', views.verse_detail, name="verse_detail"),
    url(r'^(?P<verse_id>\d+)/(?P<verse_slug>[-\w]+)/add-comment/$', views.verse_comment, name="verse_comment"),
    url(r'^(?P<verse_id>\d+)/(?P<verse_slug>[-\w]+)/like/$', views.verse_like, name="verse_like"),
    url(r'^(?P<verse_id>\d+)/(?P<verse_slug>[-\w]+)/send-email/$', views.send_verse_by_email, name="send_verse_by_email"),
]
