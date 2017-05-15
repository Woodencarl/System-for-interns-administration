from django.conf.urls import url
from .views import ViewPositions
from .views import ViewDetailPosition
from .views import close_position
from .views import ViewPositionsForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^formular/', ViewPositionsForm.as_view(), name='positionsForm'),
    url(r'^detail/(?P<position_id>\d+)/uzavrit/', login_required(close_position), name="close position"),
    url(r'^detail/(?P<position_id>\d+)/$', login_required(ViewDetailPosition.as_view()), name="detail"),
    url(r'^$', login_required(ViewPositions.as_view()), name='positions'),
]
