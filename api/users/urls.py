from django.urls import path, include
from .views import FacebookLogin, GoogleLogin, AddressViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', AddressViewSet)

urlpatterns = [
    path('login/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('login/google/', GoogleLogin.as_view(), name='google_login'),

    path('address/', include(router.urls)),

]

