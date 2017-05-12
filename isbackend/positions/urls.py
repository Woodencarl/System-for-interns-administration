from django.conf.urls import url
from .views import viewPositions
from .views import viewDetailPosition
from .views import close_position
from .views import ViewPositionsForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', ViewPositionsForm.as_view(), name='positionsForm'),
    url(r'^detail/(?P<position_id>\d+)/uzavrit/', login_required(close_position), name="close position"),
    url(r'^detail/(?P<position_id>\d+)/$', login_required(viewDetailPosition.as_view()), name="detail"),
    url(r'^$', login_required(viewPositions.as_view()), name='positions'),
]
