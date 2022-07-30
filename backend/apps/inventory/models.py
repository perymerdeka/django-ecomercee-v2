from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

# Create your models here.


class InventoryModel(models.Model):
    pass


class CategoryModel(MPTTModel):
    """
    Inventory Category Model with MPTT
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("category name"),
        null=False,
        blank=False,
        unique=True,
        help_text="format: required, max_length=100",
    )
    slug = models.SlugField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        unique=False,
        verbose_name=_("parent category"),
        help_text=_("format:  not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]
    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")
    
    def __str__(self):
        return self.name
