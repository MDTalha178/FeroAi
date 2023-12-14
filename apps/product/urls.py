"""
This file is used for urls or creating endpoint for API'S
"""
# Third party imports
from django.urls import path, include
from rest_framework import routers

# Local imports
from apps.customer.views import CustomerViewSet
from apps.product.views import ProductViewSet

router = routers.DefaultRouter()

router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path(r'product/', include(router.urls)),
]