#!/usr/bin/env python
import os
import django
import sys
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO
from django.core.files.base import ContentFile

# Setup Django
sys.path.insert(0, '/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Product

# Couleurs par catégorie
category_colors = {
    "Électronique": "#3498db",
    "Vêtements": "#e74c3c",
    "Maison & Jardin": "#2ecc71",
    "Sports & Loisirs": "#f39c12",
    "Beauté & Santé": "#9b59b6",
    "Livres": "#34495e",
}

def create_product_image(product_name, category_name):
    """Crée une image placeholder pour un produit"""
    # Couleur de la catégorie
    color = category_colors.get(category_name, "#3498db")
    
    # Convertir hex à RGB
    color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    # Créer une image
    img = Image.new('RGB', (400, 400), color_rgb)
    draw = ImageDraw.Draw(img)
    
    # Ajouter du texte
    text = product_name[:25]  # Limiter le texte
    
    # Taille de police approximative
    try:
        font_size = 30
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Position du texte
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (400 - text_width) // 2
    y = (400 - text_height) // 2
    
    # Ajouter une ombre et le texte
    draw.text((x+2, y+2), text, fill=(0, 0, 0, 100), font=font)
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Ajouter une icône/badge en bas
    draw.rectangle([10, 360, 390, 390], fill=(255, 255, 255, 150))
    draw.text((15, 365), category_name[:15], fill=(0, 0, 0), font=font)
    
    return img

# Ajouter les images aux produits
products = Product.objects.all()
success_count = 0

for product in products:
    if not product.image:
        try:
            # Créer l'image
            img = create_product_image(product.name, product.category.name)
            
            # Sauvegarder en BytesIO
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=85)
            img_io.seek(0)
            
            # Sauvegarder dans le modèle
            image_name = f"product-{product.id}.jpg"
            product.image.save(image_name, ContentFile(img_io.getvalue()), save=True)
            print(f"✓ Image créée: {product.name}")
            success_count += 1
        except Exception as e:
            print(f"✗ Erreur pour {product.name}: {str(e)}")

print("\n" + "="*50)
print(f"✅ {success_count}/{len(list(products))} images créées avec succès!")
print("="*50)
