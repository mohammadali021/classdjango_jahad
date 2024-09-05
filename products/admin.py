from django.contrib import admin
from products.models import Product, ProductCategory ,ProductInfo


class ProductInfomation(admin.ModelAdmin):
    list_display = ['color', 'slug']
    prepopulated_fields = {'slug': ('color',)}




class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'slug', 'category']
    list_filter = ['title', 'price', 'description']
    list_editable = ['price', 'category']
    readonly_fields = ['slug']
    # prepopulated_fields = {'slug': ('title',)}


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
# Register your models here.

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductInfo)
