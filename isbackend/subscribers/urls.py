from django.conf.urls import url
from .views import viewSubscribers
from .views import viewSubscribersForm
from .views import delete_sub
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', viewSubscribersForm.as_view(), name='subscribersForm'),
    url(r'^smazat/(?P<sub_id>\d+)/$', login_required(delete_sub), name="smazat odberatele"),
    url(r'^$', login_required(viewSubscribers.as_view()), name='subscribers'),

]
