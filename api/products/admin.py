from django.contrib import admin
from products.models import Product, ProductCategory, Tag


admin.site.register(ProductCategory)
admin.site.register(Tag)


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """
    On product admin site now is able to creating tags from one site
    """
    list_display = ('category', 'name', 'price', 'quantity',)
    inlines = [
        TagInline
    ]


admin.site.register(Product, ProductAdmin)

