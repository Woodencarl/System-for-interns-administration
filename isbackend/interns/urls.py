from django.conf.urls import url
from .views import InternsTable
from .views import RegisterView
from .views import ProfileView
from .views import edit_profile
from .views import create_comment
from .views import save_edit_profile
from .views import close_profile
from .views import send_to_intern
from .views import erase_profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', RegisterView.as_view(), name='internsForm'),
    url(r'^smazat/(?P<intern_id>[0-9a-f-]+)/$', erase_profile, name='smazatProfil'),
    url(r'^poslat/(?P<intern_id>[0-9a-f-]+)', send_to_intern, name="poslat"),
    url(r'^profil/(?P<intern_id>[0-9a-f-]+)/create_comment/', login_required(create_comment), name="create comment"),
    url(r'^profil/(?P<intern_id>[0-9a-f-]+)/uzavrit/', login_required(close_profile), name="close profile"),
    url(r'^profil/(?P<intern_id>[0-9a-f-]+)/editovat_profil/save/', login_required(save_edit_profile), name="save edit profile"),
    url(r'^profil/(?P<intern_id>[0-9a-f-]+)/editovat_profil/', login_required(edit_profile), name="editovat profil"),
    url(r'^profil/(?P<intern_id>[0-9a-f-]+)/$', login_required(ProfileView.as_view()), name="profil"),
    url(r'^$', login_required(InternsTable.as_view()), name='interns'),
]
