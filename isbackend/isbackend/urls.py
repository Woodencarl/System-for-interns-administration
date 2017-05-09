"""isbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staziste/', include('interns.urls')),
    url(r'^pozice/', include('positions.urls')),
    url(r'^odberatele/', include('subscribers.urls')),
    url(r'^odhlaseni/', include('login.urls')),
    url(r'^login/', auth_views.login, {'template_name': 'prihlaseni.html'}, name='prihlaseni'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'odhlaseni.html'}, name='logout'),
    url(r'^', auth_views.login, {'template_name': 'prihlaseni.html'}, name='prihlaseni'),
    # url(r'^', include('login.urls')),
]
