"""
This file is used to write business logic for customer
File Created on: 13/12/2023
"""
# framework import
from rest_framework import status
from rest_framework.response import Response

# Local imports
from apps.customer.models import Customer
from apps.customer.serializer import GetCustomerSerializer, AddCustomerSerializer, EditCustomerSerializer
from ecommerce.constant import ModelViewSet


# Create your views here.
class CustomerViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put',)
    queryset = Customer
    serializer_class = GetCustomerSerializer

    def get_queryset(self):
        queryset = self.queryset.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = AddCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': None, 'data': serializer.errors})

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        if serializer:
            return Response({'status': status.HTTP_200_OK, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_204_NO_CONTENT, 'detail': None, 'data': None})

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), many=False)
        if serializer:
            return Response({'status': status.HTTP_200_OK, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_204_NO_CONTENT, 'detail': None, 'data': None})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EditCustomerSerializer(data=request.data, context={'instance': instance})
        if serializer.is_valid():
            serializer.update(instance, request.data)
            return Response({'status': status.HTTP_200_OK, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': None, 'data': serializer.errors})
