from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('product/add/', views.product_add, name='product_add'),
    path('products/', views.product_list, name='product_list'),
    path('novelties/', views.novelties, name='novelties'),   
]