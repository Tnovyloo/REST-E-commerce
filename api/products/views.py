from rest_framework import permissions, viewsets, mixins, generics

from products.models import Product, ProductCategory, Tag
from products.serializers import \
(
    ProductSerializer,
    ProductCategorySerializer,
    ProductTagSerializer,
    TagsSerializer
)


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and Retrieve product categories
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (permissions.AllowAny,)


class TagsViewSet(generics.ListAPIView):
    """
    Retrieve tag and send products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        query_set = super().get_queryset()
        # TODO create Tags better than before.
        return query_set.filter(tags__name=self.kwargs['tag_name'])


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    """
    List and Retrieve all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
