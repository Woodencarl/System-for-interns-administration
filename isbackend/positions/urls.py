from django.conf.urls import url
from .views import viewPositions
from .views import viewPositionsForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', viewPositionsForm.as_view(), name='positionsForm'),
    url(r'^$', login_required(viewPositions.as_view()), name='positions'),

]