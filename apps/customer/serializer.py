import logging

from rest_framework import serializers

from apps.customer.models import Customer


class GetCustomerSerializer(serializers.ModelSerializer):
    """
    This serializer is to get customer details
    """

    class Meta:
        model = Customer
        fields = '__all__'


class AddCustomerSerializer(serializers.ModelSerializer):
    """
    This serializer is used to create a customer data
    """
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    contact_number = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    email = serializers.CharField(required=True, allow_null=False, allow_blank=False)

    @staticmethod
    def validate_email(value):
        """
        this method is used to validate an email
        :param value:
        :return:
        """
        if Customer.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError({'Email': 'Email already exists'})
        return value

    @staticmethod
    def validate_name(value):
        """
        this method is used to validate customer name is already exists in our application
        :param value: name
        :return:
        """
        if Customer.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError({'Name': 'Name already exists'})
        return value

    def create(self, validated_data):
        """
        this method will create data for customer
        :param validated_data:
        :return: customer obj
        """
        customer_obj = Customer.objects.create(**validated_data)
        return customer_obj

    class Meta:
        model = Customer
        fields = ('name', 'contact_number', 'email',)


class EditCustomerSerializer(AddCustomerSerializer):
    """
    this serializer class is used to update a customer data
    """
    def update(self, instance, validated_data):
        try:
            Customer.objects.filter(id=instance.id).update(**validated_data)
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError(e)

    class Meta:
        model = Customer
        fields = ('name', 'contact_number', 'email',)
