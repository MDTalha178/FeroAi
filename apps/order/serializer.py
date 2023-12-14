import logging

from django.utils import timezone
from rest_framework import serializers

from apps.customer.models import Customer
from apps.order.models import Order, OrderItem
from apps.product.models import Product
from ecommerce.constant import generate_order_number


class GetAllOrderDetailsSerialzier(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class GetOrderSerializer(serializers.ModelSerializer):
    """
    This serializer is to get order details
    """
    order_details = serializers.SerializerMethodField()

    def get_order_details(self, obj):
        """
        this method is used to get all orders
        :return:
        """
        order_obj = None
        order_obj = OrderItem.objects.filter(order_id=obj.id)
        if order_obj:
            order_obj = GetAllOrderDetailsSerialzier(order_obj, many=True).data
        return order_obj

    class Meta:
        model = Order
        fields = '__all__'


class AddOrderSerializer(serializers.ModelSerializer):
    """
    This serializer is to create order details
    """
    customer = serializers.PrimaryKeyRelatedField(
        required=True, allow_null=False, allow_empty=False, queryset=Customer.objects.filter())
    order_date = serializers.DateField(required=True, allow_null=False)
    address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    order_item = serializers.ListField(required=True, allow_null=False, allow_empty=False)

    def validate(self, data):
        """
        this method is used to validate date and product weight
        :param data:
        :return:
        """
        order_items = data.get('order_item', [])
        order_date = data.get('order_date')
        if order_date and order_date < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        product_weights = Product.objects.filter(
            id__in=[item['product'] for item in order_items]
        ).values('id', 'weight')
        product_weight_dict = {item['id']: item['weight'] for item in product_weights}
        print(product_weight_dict)
        cumulative_weight = sum(
            int(item['quantity']) * product_weight_dict[int(item['product'])] for item in order_items)
        print(cumulative_weight)
        if cumulative_weight > 150:
            raise serializers.ValidationError("Order cumulative weight exceeds the limit of 150kg.")
        return data

    def create(self, validated_data):
        """
        this method is used to create an order
        :param validated_data:
        :return:
        """
        try:
            order_number = generate_order_number()
            order_obj = Order.objects.create(
                order_number=order_number,
                customer_id=validated_data['customer'].id,
                order_date=validated_data['order_date'],
                address=validated_data['address']
            )
            if order_obj:
                order_items = [
                    OrderItem(order_id=order_obj.id, product_id=item['product'], quantity=item['quantity'])
                    for item in validated_data['order_item']
                ]
                OrderItem.objects.bulk_create(order_items)
            return order_obj
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError(e)

    class Meta:
        model = Order
        fields = '__all__'


class EditOrderSerializer(AddOrderSerializer):
    """
    this class is used to edit order
    """

    def update(self, instance, validated_data):
        try:
            Order.objects.filter(instance.id).update(
                customer_id=validated_data['customer'],
                order_date=validated_data['order_date'],
                address=validated_data['address']
            )
            order_items = validated_data['order_item']
            for index, item in enumerate(order_items):
                order_items[index].product_id = item['product']
                order_items[index].quantity = item['quantity']

            OrderItem.objects.bulk_update(order_items, ['product_id', 'quantity'])
        except Exception as e:
            logging.error(e)

    class Meta:
        model = Order
        fields = ('customer_id', 'order_date', 'address', 'order_item',)
