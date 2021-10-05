from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Server(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=24)
    description = models.CharField(max_length=240)