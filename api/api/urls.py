"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from dj_rest_auth.registration.views import VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView, LogoutView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', include('products.urls', namespace='products')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('user/auth/', include('dj_rest_auth.urls')),
    path('user/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('user/', include('users.urls')),
    path('user/resend-email/', ResendEmailVerificationView.as_view(),
         name="rest_resend_email"),
    re_path(
        r'^user/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email',
    ),
    path(
        'user/account-email-verification-sent/', TemplateView.as_view(),
        name='account_email_verification_sent',
    ),
    path('user/orders/',
         include('orders.urls', namespace='orders')),
]


# Media Assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Schema URLs
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
]
