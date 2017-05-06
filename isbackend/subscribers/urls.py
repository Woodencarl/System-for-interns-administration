from django.conf.urls import url
from .views import viewSubscribers
from .views import viewSubscribersForm

urlpatterns = [
    url(r'^formular/', viewSubscribersForm.as_view(), name='subscribersForm'),
    url(r'^$', viewSubscribers.as_view(), name='subscribers'),

]