from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True)
    is_member = models.BooleanField(blank=True, null=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
