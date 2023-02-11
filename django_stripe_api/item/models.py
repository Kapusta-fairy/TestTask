from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    pass
