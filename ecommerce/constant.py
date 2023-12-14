"""
This file is used to store constant or common classes and function
"""
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from apps.order.models import Order


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass


class CustomFilterBackend(DjangoFilterBackend):
    """
    this is custom filter backend
    """

    def filter_queryset(self, request, queryset, view):
        """
        this method is used to filter queryset
        :param request:
        :param queryset:
        :param view:
        :return:
        """
        customer = request.query_params.get('customer')
        if customer:
            customer = customer.split(',')
            queryset = queryset.filter(customer__name__in=customer)
        return queryset


class ProductFilterBackend(DjangoFilterBackend):
    """
        this is custom filter backend
    """

    def filter_queryset(self, request, queryset, view):
        """
        this method is used to filter queryset
        :param request:
        :param queryset:
        :param view:
        :return:
        """
        product = request.query_params.get('product')
        if product:
            product = product.split(',')
            queryset = queryset.filter(name__in=product)
        return queryset


def generate_order_number():
    """
    this method is used generate an order
    :return:
    """
    last_order = Order.objects.order_by('-id').first()
    last_number = 0 if not last_order else int(last_order.order_number[3:])
    new_number = last_number + 1
    order_number = f'ORD{new_number:05d}'
    return order_number
