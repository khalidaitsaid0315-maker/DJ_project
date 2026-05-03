from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:pk>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]
