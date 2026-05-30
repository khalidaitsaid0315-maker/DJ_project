from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from products.models import Product


def index(request):
    return render(request, 'executer/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'executer/product_list.html', {'products': products})


def execute_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Perform a lightweight 'execute' action: return product details as JSON
    data = {
        'id': product.id,
        'name': product.name,
        'price': float(product.price),
        'message': f'Product {product.name} executed successfully.'
    }
    return JsonResponse(data)
