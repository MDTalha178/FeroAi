from django.contrib import admin

# Register your models here.
from apps.product.models import Product
admin.site.register(Product)
