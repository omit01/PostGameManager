"""PostGameManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as views_auth
from django.urls import path

urlpatterns = [
    url(r'^login/$', views_auth.LoginView.as_view(), {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', views_auth.LogoutView.as_view(), {'template_name': 'core/logged_out.html'}, name='logout'),
    url('admin/', admin.site.urls),
]
