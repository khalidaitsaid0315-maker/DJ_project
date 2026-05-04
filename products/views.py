from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
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

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:3]
    
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'products/product_detail.html', context)

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.stock <= 0:
        messages.warning(request, "Ce produit est en rupture de stock.")
        return redirect('product_detail', pk=product.pk)

    cart = request.session.get('cart', {})
    product_id = str(product.pk)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    messages.success(request, f"{product.name} a ete ajoute au panier.")
    return redirect(request.POST.get('next') or 'cart')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(str(pk), None)
    request.session['cart'] = cart
    messages.success(request, "Produit retire du panier.")
    return redirect('cart')

def cart(request):
    cart_data = request.session.get('cart', {})
    products = Product.objects.filter(pk__in=cart_data.keys())
    items = []
    total = 0

    for product in products:
        quantity = cart_data.get(str(product.pk), 0)
        subtotal = product.price * quantity
        total += subtotal
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'products/cart.html', {
        'items': items,
        'total': total,
    })

def add_to_favorites(request, pk):
    product = get_object_or_404(Product, pk=pk)
    favorites = request.session.get('favorites', [])
    product_id = str(product.pk)

    if product_id not in favorites:
        favorites.append(product_id)
        request.session['favorites'] = favorites
        messages.success(request, f"{product.name} a ete ajoute aux favoris.")
    else:
        messages.info(request, f"{product.name} est deja dans vos favoris.")

    return redirect(request.POST.get('next') or 'favorites')

def remove_from_favorites(request, pk):
    favorites = request.session.get('favorites', [])
    product_id = str(pk)
    if product_id in favorites:
        favorites.remove(product_id)
        request.session['favorites'] = favorites
        messages.success(request, "Produit retire des favoris.")
    return redirect('favorites')

def favorites(request):
    favorite_ids = request.session.get('favorites', [])
    products = Product.objects.filter(pk__in=favorite_ids)
    return render(request, 'products/favorites.html', {'products': products})

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
