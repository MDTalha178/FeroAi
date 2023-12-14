"""
This is used to create a table into database for storing a customer details
File Created on: 13/12/2023
"""
# framework import
from django.db import models

# Create your models here.
# Local imports
from apps.customer.models import Customer
from apps.product.models import Product


class Order(models.Model):
    """
    Do: This class will create an order table into a database
    purpose: In this table we store an order info
    """
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    class Meta:
        db_table = "order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "order_item"
