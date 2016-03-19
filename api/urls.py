from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, FlightViewSet, AirportViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'airports', AirportViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^api-token-auth/', csrf_exempt(obtain_auth_token))
]
