from django.urls import path
from .views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('login/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('login/google/', GoogleLogin.as_view(), name='google_login'),
]

