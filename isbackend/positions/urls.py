from django.conf.urls import url
from .views import viewPositions
from .views import viewPositionsForm

urlpatterns = [
    url(r'^formular/', viewPositionsForm.as_view(), name='positionsForm'),
    url(r'^$', viewPositions.as_view(), name='positions'),

]