"""PostGameManager URL Configuration"""
# TODO Modify urls for editing en deleting groups, posts and rounds

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as views_auth
from django.urls import path
import views

urlpatterns = [
    path('', views.index, name='index'),

    url(r'^login/$', views_auth.LoginView.as_view(), {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', views_auth.LogoutView.as_view(), {'template_name': 'core/logged_out.html'}, name='logout'),
    url('admin/', admin.site.urls),

    path('post/<uuid:uuid>/', views.views_post.main, name='post'),

    path('central/', views.views_general.main, name='central post'),
    path('central/standings/', views.views_general.standings, name='standings'),
    path('central/setup/', views.views_general.settings, name='settings'),
    path('central/setup/addgroup', views.views_general.addgroup, name='add group'),
    path('central/setup/addpost', views.views_general.addpost, name='add post')
]
