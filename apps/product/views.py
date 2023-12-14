"""
This file is used to write business logic for customer
File Created on: 13/12/2023
"""
# framework import
from rest_framework import status
from rest_framework.response import Response

# Local imports
from apps.product.models import Product
from apps.product.serializer import AddProductSerializer, EditProductSerializer, GetProductSerializer
from ecommerce.constant import ModelViewSet, ProductFilterBackend


# Create your views here.
class ProductViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put',)
    queryset = Product
    serializer_class = GetProductSerializer
    filter_backends = (ProductFilterBackend,)

    def get_queryset(self):
        queryset = self.queryset.objects.all()
        queryset = self.filter_queryset(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = AddProductSerializer(data=request.data)
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
        serializer = EditProductSerializer(data=request.data, context={'instance': instance})
        if serializer.is_valid():
            serializer.update(instance, request.data)
            return Response({'status': status.HTTP_200_OK, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': None, 'data': serializer.errors})
