from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


def category_image_path(instance, filename):
    return f'product/category/icons/{instance.name}/{filename}'


def product_image_path(instance, filename):
    return f'product/images/{instance.name}/{filename}'


class ProductCategory(models.Model):
    """Product category model"""
    name = models.CharField(_("Category name"), max_length=100)
    icon = models.ImageField(upload_to=category_image_path, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.name


def get_default_product_category():
    """Returning object in tuple"""
    return ProductCategory.objects.get_or_create(name="Others")[0]


class Tag(models.Model):
    """Tag model for filtering objects"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(ProductCategory,
                                 related_name="product_list",
                                 on_delete=models.SET(get_default_product_category))
    name = models.CharField(max_length=200)
    desc = models.TextField(_("Description"), blank=True)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name

