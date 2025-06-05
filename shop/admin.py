from django.contrib import admin
from .models import Category, Product, Supplier, SupplierProduct, Favorite

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(SupplierProduct)
admin.site.register(Favorite)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')  # Отображаемые поля
    list_filter = ('category', 'created_at')  # Фильтры
    search_fields = ('name', 'description')  # Поиск