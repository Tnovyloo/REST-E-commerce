from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductCategoryViewSet, ProductViewSet, TagsViewSet

app_name = 'products'

router = DefaultRouter()
router.register(r'categories', ProductCategoryViewSet)
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tags/<slug:tag_name>/', TagsViewSet.as_view())
]

