from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse
from product.models import Product

class Income(models.Model):
    total_revenue = models.DecimalField(max_digits=20, null=True, decimal_places=2,default=0.0)
    total_cost = models.DecimalField(max_digits=20, null=True, decimal_places=2)

    data_create = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    growth_revenue = models.FloatField(null=True, default=0.0)
    growth_cost = models.FloatField(null=True, default=0.0)
    growth_profit = models.FloatField(null=True, default=0.0)


    def __str__(self):
        return str(self.data_create.year) + str("-") + str(self.data_create.month)

    def total_profit(self):
        return self.total_revenue - self.total_cost

    def save(self, *args, **kwargs):
        self.growth_revenue = round(self.growth_revenue, 2)
        self.growth_cost = round(self.growth_cost, 2)
        self.growth_profit = round(self.growth_profit, 2)
        super(Income, self).save(*args, **kwargs)


class Bill(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(default=30.0, max_digits=8, null=True, decimal_places=2)
    date_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.date_create.year) + str("-") + str(self.date_create.month) + str("-") + str(
            self.date_create.day)

    def nameProduct(self):
        return self.product.title

