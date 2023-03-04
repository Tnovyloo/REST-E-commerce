from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for product categories
    """
    class Meta:
        model = ProductCategory
        fields = ['name', 'icon']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for products
    """
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['category', 'name', 'desc', 'image', 'price']
