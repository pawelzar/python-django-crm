from django.conf.urls import url
from .views import user as user_views
from .views import company as comp_views
from .views import auth as auth_views


urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/', user_views.profile_view, name='profile'),
    url(r'^companies/', comp_views.company_list, name='company_list'),
    url(r'^company/(?P<pk>[0-9]+)/$', comp_views.company_details, name='company_details'),
    url(r'^company/new/$', comp_views.company_new, name='company_new'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', comp_views.company_edit, name='company_edit'),
    url(r'^users/', user_views.users_list, name='users_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', user_views.user_details, name='user_details'),
    url(r'^user/new/$', user_views.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', user_views.user_edit, name='user_edit'),
]
