from django.conf.urls import url
from .views import ViewSubscribers
from .views import ViewSubscribersForm
from .views import delete_sub
from .views import download_csv
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', ViewSubscribersForm.as_view(), name='subscribersForm'),
    url(r'^exportCSV/', login_required(download_csv), name='download CSV'),
    url(r'^smazat/(?P<sub_id>[0-9a-f-]+)/$', delete_sub, name='smazat'),
    url(r'^$', login_required(ViewSubscribers.as_view()), name='subscribers'),
]
