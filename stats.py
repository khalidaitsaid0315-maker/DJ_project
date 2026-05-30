#!/usr/bin/env python
import os
import django
import sys

sys.path.insert(0, '/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Product, Category

categories = Category.objects.count()
products = Product.objects.count()
products_with_images = Product.objects.exclude(image='').count()

print("\n" + "="*50)
print("✅ STATISTIQUES FINALES DE L'APPLICATION")
print("="*50)
print(f"✓ Catégories: {categories}")
print(f"✓ Produits totaux: {products}")
print(f"✓ Produits avec images: {products_with_images}")
print("="*50 + "\n")
