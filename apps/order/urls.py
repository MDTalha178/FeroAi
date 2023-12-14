"""
This file is used for urls or creating endpoint for API'S
"""
# Third party imports
from django.urls import path, include
from rest_framework import routers

# Local imports
from apps.customer.views import CustomerViewSet
from apps.order.views import OrderViewSet

router = routers.DefaultRouter()

router.register('', OrderViewSet, basename='order')

urlpatterns = [
    path(r'order/', include(router.urls)),
]