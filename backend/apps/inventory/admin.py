from django.contrib import admin
from apps.inventory.models import InventoryModel, CategoryModel

# Register your models here.


class InventoryModelAdmin(admin.ModelAdmin):
    pass

class CategoryModelAdmin(admin.ModelAdmin):
    pass


# register model admin

admin.site.register(InventoryModel, InventoryModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)