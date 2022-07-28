from django.db import models

# Create your models here.

class InventoryModel(models.Model):
    pass

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(default=True)