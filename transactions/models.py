from django.db import models
from django.db.models.fields.related import ManyToManyField, OneToOneField
from aktor.models import Employee, Customer, Item

class ItemOrder(models.Model):
    item = OneToOneField(Item, on_delete=models.RESTRICT)
    sub_total = models.PositiveIntegerField()

# Create your models here.
class Order(models.Model):
    clerk = OneToOneField(Employee, on_delete=models.CASCADE)
    customer = OneToOneField(Customer, on_delete=models.CASCADE)
    total_item = ManyToManyField(ItemOrder, related_name='total_item')
