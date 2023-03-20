from rest_framework import permissions, viewsets, mixins

from products.models import Product, ProductCategory
from products.serializers import ProductSerializer, ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny, )


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    """
    List and Retrieve all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
