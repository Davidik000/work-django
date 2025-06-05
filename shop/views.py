from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Product, Favorite, Category, SupplierProduct

def index(request):
    # Поиск
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        # Топ-5 товаров
        products = Product.objects.all().order_by('-created_at')[:5]

    # Подсчёт избранных товаров (для статистики)
    favorite_counts = Product.objects.annotate(favorite_count=Count('favorite')).filter(favorite_count__gt=0)

    return render(request, 'shop/index.html', {
        'products': products,
        'search_query': search_query,
        'favorite_counts': favorite_counts,
    })

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if Favorite.objects.filter(user=request.user, product=product).exists():
        Favorite.objects.filter(user=request.user, product=product).delete()
        messages.success(request, "Товар удалён из избранного!")
    else:
        Favorite.objects.create(user=request.user, product=product)
        messages.success(request, "Товар добавлен в избранное!")
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    suppliers = SupplierProduct.objects.filter(product=product)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'suppliers': suppliers,
        'is_favorite': is_favorite,
    })

@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.name_en = request.POST.get('name_en')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        category_id = request.POST.get('category')
        product.category = get_object_or_404(Category, id=category_id)
        product.save()
        messages.success(request, "Товар обновлён!")
        return redirect('product_detail', product_id=product.id)
    return render(request, 'shop/product_edit.html', {
        'product': product,
        'categories': categories,
    })

@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Товар удалён!")
        return redirect('index')
    return render(request, 'shop/product_delete.html', {'product': product})

@login_required
def product_add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        name_en = request.POST.get('name_en')
        description = request.POST.get('description')
        image = request.POST.get('image')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)
        product = Product.objects.create(
            name=name,
            name_en=name_en,
            description=description,
            image=image,
            category=category,
        )
        messages.success(request, "Товар добавлен!")
        return redirect('product_detail', product_id=product.id)
    return render(request, 'shop/product_add.html', {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def novelties(request):
    novelties_list = Product.objects.order_by('-created_at')[:5]  # Топ-5 самых новых товаров
    return render(request, 'shop/novelties.html', {'novelties': novelties_list})

