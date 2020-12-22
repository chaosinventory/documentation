from django.db import models

class Location(models.model):
    location = models.ForeignKey('self', on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    note = models.TextField()

class Asset(models.model):
    name = models.CharField(max_length=30)
    note = models.TextField()
    metadata = models.JSONField()

class Item(models.model):
    parent = models.ForeignKey('self' , on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    tags = models.ManyToManyField(InventoryTag)
    amount = models.IntegerField()

class InventoryTag(models.model):
    tag = models.CharField(max_length=32)

