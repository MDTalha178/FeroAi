# framework import
from rest_framework import status
from rest_framework.response import Response

# Local Imports
from apps.order.models import Order
from apps.order.serializer import GetOrderSerializer, AddOrderSerializer, EditOrderSerializer
from ecommerce.constant import ModelViewSet, CustomFilterBackend


# Create your views here.
class OrderViewSet(ModelViewSet):
    """
    this class is used for order create get update and delete
    """
    http_method_names = ('get', 'post',)
    queryset = Order
    serializer_class = GetOrderSerializer
    filter_backends = (CustomFilterBackend,)

    def get_queryset(self):
        queryset = self.queryset.objects.filter()
        queryset = self.filter_queryset(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = AddOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'detail': None, 'data': None})
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
        serializer = EditOrderSerializer(data=request.data, context={'instance': instance})
        if serializer.is_valid():
            serializer.update(instance, request.data)
            return Response({'status': status.HTTP_200_OK, 'detail': None, 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'detail': None, 'data': serializer.errors})
