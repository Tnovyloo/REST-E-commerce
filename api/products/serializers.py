from rest_framework import serializers

from products.models import Product, ProductCategory, Tag


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for product categories
    """
    class Meta:
        model = ProductCategory
        fields = ['name', 'icon']


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tags
    """
    class Meta:
        model = Tag
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for products
    """
    category = serializers.CharField(source='category.name', read_only=True)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['category', 'tags', 'name', 'desc', 'image', 'price']

