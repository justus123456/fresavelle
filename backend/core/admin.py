from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'unit', 'price_kobo', 'stock', 'is_basket', 'active')
    list_filter = ('category', 'is_basket', 'active')
    search_fields = ('name',)

admin.site.site_header = 'Fresavelle — local development controls'
admin.site.site_title = 'Local development only'
admin.site.index_title = 'Sample catalogue and stock'
