from django.db import models
from django.contrib.auth.models import User

# Модель категории продуктов
class Category(models.Model):
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Модель продукта
class Product(models.Model):
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Модель поставщика
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Связь между поставщиками и продуктами
class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('supplier', 'product')

# Модель избранного
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"