"""
This file is used for urls or creating endpoint for API'S
"""
# Third party imports
from django.urls import path, include
from rest_framework import routers

# Local imports
from apps.customer.views import CustomerViewSet

router = routers.DefaultRouter()

router.register('', CustomerViewSet, basename='customer')

urlpatterns = [
    path(r'customer/', include(router.urls)),
]