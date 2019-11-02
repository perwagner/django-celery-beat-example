from django.db import models


class Order(models.Model):
    product = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
