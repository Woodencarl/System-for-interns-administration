from django.conf.urls import url
from .views import viewSubscribers
from .views import viewSubscribersForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', viewSubscribersForm.as_view(), name='subscribersForm'),
    url(r'^$', login_required(viewSubscribers.as_view()), name='subscribers'),

]