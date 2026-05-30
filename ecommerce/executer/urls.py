from django.urls import path
from . import views

app_name = 'executer'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/execute/', views.execute_product, name='execute_product'),
]
