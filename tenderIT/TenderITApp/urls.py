from django.conf.urls import patterns, url
from django.contrib.auth.views import (login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
from TenderITApp import views

# content related urls
urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^project_view/$', views.project_view, name="project_view"),
    url(r'^company/(?P<company_id>[\w\-]+)/$', views.company, name="company"),
    url(r'^project/(?P<project_pk>[\w\-]+)/$', views.project, name="project"),
    url(r'^companies/$', views.companies, name="companies"),
    url(r'^post_project/$', views.post_project, name="post_project "),
    url(r'^(?P<project_id>[0-9]+)/$', views.apply_project, name="apply_project")
    )



# account related urls
urlpatterns += (
    url(r'^register/$', views.register_user, name="register"),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logged_in/$', views.logged_in, name="logged_in"),
    url(r'^logout/$', logout,{'template_name': 'registration/log_out.html'}, name="logout"),
    url(r'^password-change/$', password_change,
        {'template_name': 'registration/password_change.html'}, name='password_change'),
    url(r'^password_change/done/$', password_change_done,
        {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),
    url(r'^password-reset/$', password_reset,
        {'template_name': 'registration/password_reset.html'}, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done,
        {'template_name': 'registration/password_rst_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm, {'template_name': 'registration/password_rst_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete,
        {'template_name': 'registration/password_rst_complete.html'}, name='password_reset_complete')
    )
