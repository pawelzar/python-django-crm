from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.company_list, name='company_list'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^company/new/$', views.company_new, name='company_new'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', views.company_edit, name='company_edit'),
    url(r'^accounts/login/', auth_views.login, {'template_name': 'crm/login.html'}),
    url(r'^accounts/profile/', views.company_list, name='profile'),
    url(r'^logout/$', views.logout_view, name='login'),
]
