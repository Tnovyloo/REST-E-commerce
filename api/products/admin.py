from django.contrib import admin
from products.models import Product, ProductCategory, Tag


admin.site.register(ProductCategory)
admin.site.register(Tag)


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin View
    """
    list_display = ('category', 'name', 'price', 'quantity',)


admin.site.register(Product, ProductAdmin)

