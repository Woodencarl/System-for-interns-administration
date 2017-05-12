"""webapp URL Configuration

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
from django.conf.urls import url
from .views import InternsTable
from .views import RegisterView
from .views import ProfileView
from .views import edit_profile
from .views import create_comment
from .views import save_edit_profile
from .views import close_profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', RegisterView.as_view(), name='internsForm'),
    url(r'^profil/(?P<intern_id>\d+)/create_comment/', login_required(create_comment), name="create comment"),
    url(r'^profil/(?P<intern_id>\d+)/uzavrit/', login_required(close_profile), name="close profile"),
    url(r'^profil/(?P<intern_id>\d+)/editovat_profil/save/', login_required(save_edit_profile), name="save edit profile"),
    url(r'^profil/(?P<intern_id>\d+)/editovat_profil/', login_required(edit_profile), name="editovat profil"),
    url(r'^profil/(?P<intern_id>\d+)/$', login_required(ProfileView.as_view()), name="profil"),
    url(r'^$', login_required(InternsTable.as_view()), name='interns'),
]
