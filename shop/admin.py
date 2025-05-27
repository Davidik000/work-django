from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Category, Product, Supplier, SupplierProduct, Order, OrderItem, Review, Discount, DiscountHistory, Payment, Address

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(SupplierProduct)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Discount)
admin.site.register(DiscountHistory)
admin.site.register(Payment)
admin.site.register(Address)
