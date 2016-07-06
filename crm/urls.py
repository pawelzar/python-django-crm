from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'crm/login.html'}),
    url(r'^company/(?P<pk>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^company/new/$', views.company_new, name='company_new'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', views.company_edit, name='company_edit'),
    url(r'^accounts/profile/', views.profile_view, name='profile'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^companies/', views.company_list, name='company_list'),
    url(r'^users/', views.users_list, name='users_list'),
]
