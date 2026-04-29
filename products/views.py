from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Search
    query = request.GET.get('q', '')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    # Filter by category
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        products = products.filter(category__id__in=selected_categories)
    
    # Sort
    sort = request.GET.get('sort', 'newest')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:  # newest
        products = products.order_by('-created_at')
    
    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_categories': selected_categories,
        'sort': sort,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:3]
    
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'products/product_detail.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    products = category.products.all()
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })