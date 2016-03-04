from django.conf.urls import patterns, url
from django.contrib.auth.views import (password_change, password_change_done, password_reset,
                                       password_reset_done, password_reset_confirm, password_reset_complete)

from .views import (content_views, rgstr_views)


# content related urls
urlpatterns = patterns('content_views',
    url(r'^$', content_views.index, name="index"),
    url(r'^project_view/$', content_views.project_view, name="project_view"),
    url(r'^company/(?P<company_id>[\w\-]+)/$', content_views.company, name="company"),
    url(r'^companies/$', content_views.companies, name="companies"),
    url(r'^post_project/$', content_views.post_project, name="post_project "),
    url(r'^(?P<project_id>[0-9]+)/$', content_views.apply_project, name="apply_project")
    )



# account related urls
urlpatterns += (
    url(r'^register/$', rgstr_views.register_user, name="register"),
    url(r'^login/$', rgstr_views.login, name="login"),
    url(r'^logout/$', rgstr_views.logout, name="logout"),
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