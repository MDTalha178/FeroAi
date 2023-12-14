"""
This is used to create a table into database for storing a customer details
File Created on: 13/12/2023
"""

# framework imports
from django.db import models


# Create your models here.
class Customer(models.Model):
    """
    Do: This class will create a customer table into a database
    purpose: In this table we store a basic customer info
    """
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "customer"
