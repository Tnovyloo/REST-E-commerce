from rest_framework import serializers
from .models import Address
from .permissions import IsUserAddressOwner


class AddressReadOnlySerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Address model
    """
    user = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize address of type shipping

    For shipping address automatically set address type to shipping
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('address_type', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address_type'] = 'S'

        return representation


class BillingAddressSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize address of type billing

    For billing address, automatically set address type to billing
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('address_type', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address_type'] = 'B'

        return representation
