from django.db import models

from product.models import *
from register.models import *
# Create your models here.
import string
import random


def generate_unique_code():
    length = 12

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Order.objects.filter(transaction_id=code).count() == 0:
            break

    return code
class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=12,default=generate_unique_code, null=True,unique=True)
    discount = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return str(self.transaction_id)

    def get_total_item(self):
        order = self.orderitem_set.all()
        total = float(sum([item.get_total for item in order]))*(1-(self.discount/100.0))
        return total

    def get_total_order(self):
        order = self.orderitem_set.all()
        total = (sum([item.quantity for item in order]))
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='detail',on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=100, null=True)
    price = models.IntegerField()

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    def detail(self):
        detail = Product.objects.all().filter(title = self.product.title)
        # a={"title":"","image":""}
        a = ""
        for i in detail:
            a= str(i.title)

        return a

    def __str__(self):
        return str(self.order.transaction_id)

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    country=models.ForeignKey(Country, on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.country.name