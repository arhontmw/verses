from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_change, password_change_done, \
                                      password_reset, password_reset_done, \
                                      password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^$', views.render_main_page, name="render_main"),
    url(r'^login/$', views.user_login, name="login"),
    # url(r'^login/(?P<auth_status>[\w]+)/$', views.user_login, name="login_again"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^registration/$', views.user_register, name="register"),
    url(r'^need-login/$', views.need_login, name="need_login"),
    url(r'^user/(?P<user_id>\d+)/$', views.user_page, name="user_page"),
    url(r'^user/edit/(?P<user_id>\d+)/$', views.edit_user_page, name="edit_user_page"),
]
