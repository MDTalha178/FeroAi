import logging

from rest_framework import serializers
from decimal import Decimal
from apps.product.models import Product


class GetProductSerializer(serializers.ModelSerializer):
    """
    This serializer is to get customer details
    """

    class Meta:
        model = Product
        fields = '__all__'


class AddProductSerializer(serializers.ModelSerializer):
    """
    this serializer class is used to create product
    """
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    weight = serializers.DecimalField(required=True, allow_null=True, max_digits=5, decimal_places=2,)

    @staticmethod
    def validate_weight(value):
        print(type(value))
        if value is not None:
            if not isinstance(value, (int, Decimal)) or value <= 0:
                raise serializers.ValidationError("Weight must be a positive number.")
            elif value > 25:
                raise serializers.ValidationError("Weight must not be more than 25kg.")
        return value

    @staticmethod
    def validate_name(value):
        """
        this method is used to validate product name
        :return:
        """
        if Product.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError({'Product': 'Product name already exists'})
        return value

    def create(self, validated_data):
        try:
            product_obj = Product.objects.create(**validated_data)
            return product_obj
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError(e)

    class Meta:
        model = Product
        fields = ('name', 'weight',)


class EditProductSerializer(AddProductSerializer):
    """
    this serializer class is used edit product name
    """
    def update(self, instance, validated_data):
        try:
            Product.objects.filter(id=instance.id).update(**validated_data)
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError(e)

    class Meta:
        model = Product
        fields = ('name', 'weight',)
