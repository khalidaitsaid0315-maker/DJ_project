#!/usr/bin/env python
import os
import django
import sys

# Setup Django
sys.path.insert(0, '/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Product
from decimal import Decimal

# Clear existing products (optional)
Product.objects.all().delete()
Category.objects.all().delete()

# Create categories
categories_data = [
    "Électronique",
    "Vêtements",
    "Maison & Jardin",
    "Sports & Loisirs",
    "Beauté & Santé",
    "Livres",
]

categories = {}
for cat_name in categories_data:
    cat = Category.objects.create(name=cat_name)
    categories[cat_name] = cat
    print(f"✓ Catégorie créée: {cat_name}")

# Create products
products_data = [
    # Électronique
    {
        "name": "Smartphone Samsung Galaxy S24",
        "description": "Téléphone dernière génération avec écran AMOLED 120Hz, processeur Snapdragon 8 Gen 3, batterie 5000mAh, caméra 200MP",
        "price": Decimal("999.99"),
        "stock": 15,
        "category": "Électronique"
    },
    {
        "name": "Écouteurs Sony WH-1000XM5",
        "description": "Écouteurs sans fil premium avec réduction de bruit active, batterie 30h, son haute résolution",
        "price": Decimal("349.99"),
        "stock": 25,
        "category": "Électronique"
    },
    {
        "name": "MacBook Pro 16 pouces",
        "description": "Ordinateur portable premium, processeur Apple M3 Pro, 16GB RAM, 512GB SSD, écran Retina",
        "price": Decimal("2499.99"),
        "stock": 8,
        "category": "Électronique"
    },
    {
        "name": "Tablette iPad Air",
        "description": "Tablette 11 pouces avec processeur M1, écran Liquid Retina, batterie 15 heures, Apple Pencil compatible",
        "price": Decimal("649.99"),
        "stock": 12,
        "category": "Électronique"
    },
    
    # Vêtements
    {
        "name": "Veste Adidas Ultraboost",
        "description": "Veste de sport légère et imperméable, technologie Climacool, design moderne",
        "price": Decimal("119.99"),
        "stock": 40,
        "category": "Vêtements"
    },
    {
        "name": "Jeans Levi's 501",
        "description": "Jean classique 100% coton, coupe intemporelle, confection robuste",
        "price": Decimal("79.99"),
        "stock": 50,
        "category": "Vêtements"
    },
    {
        "name": "T-shirt Nike Blanc Premium",
        "description": "T-shirt 100% coton biologique, col rond, logo brodé Nike, taille unisexe",
        "price": Decimal("34.99"),
        "stock": 75,
        "category": "Vêtements"
    },
    {
        "name": "Robe Été Fleurie",
        "description": "Robe légère et confortable, design floral, tissu respirant, idéale pour l'été",
        "price": Decimal("54.99"),
        "stock": 30,
        "category": "Vêtements"
    },
    
    # Maison & Jardin
    {
        "name": "Lampe Tactile LED RGB",
        "description": "Lampe multicolore contrôlable par geste, 16 millions de couleurs, USB rechargeable",
        "price": Decimal("29.99"),
        "stock": 35,
        "category": "Maison & Jardin"
    },
    {
        "name": "Miroir Mural Décoratif",
        "description": "Miroir carré or, design moderne, 80x80cm, verre haute qualité",
        "price": Decimal("89.99"),
        "stock": 20,
        "category": "Maison & Jardin"
    },
    {
        "name": "Coussin Velours Gris",
        "description": "Coussin décoratif 45x45cm, velours premium, remplissage confortable",
        "price": Decimal("24.99"),
        "stock": 60,
        "category": "Maison & Jardin"
    },
    {
        "name": "Tapis Persan Authentique",
        "description": "Tapis tissé main, laine naturelle, motifs traditionnels, 200x300cm",
        "price": Decimal("299.99"),
        "stock": 5,
        "category": "Maison & Jardin"
    },
    
    # Sports & Loisirs
    {
        "name": "Vélo Mountain Bike",
        "description": "VTT 29 pouces, 21 vitesses, suspension avant, freins à disque hydrauliques",
        "price": Decimal("449.99"),
        "stock": 10,
        "category": "Sports & Loisirs"
    },
    {
        "name": "Tapis de Yoga Premium",
        "description": "Tapis écologique TPE non-glissant, 180x60cm, épaisseur 6mm",
        "price": Decimal("44.99"),
        "stock": 45,
        "category": "Sports & Loisirs"
    },
    {
        "name": "Haltères Ajustables 20kg",
        "description": "Paire d'haltères réglables 1-20kg, chrome, poignée ergonomique",
        "price": Decimal("99.99"),
        "stock": 22,
        "category": "Sports & Loisirs"
    },
    {
        "name": "Ballon de Football Officiel",
        "description": "Ballon FIFA approved, cuir synthétique, machine à coudre, taille 5",
        "price": Decimal("39.99"),
        "stock": 55,
        "category": "Sports & Loisirs"
    },
    
    # Beauté & Santé
    {
        "name": "Crème Visage Hydratante",
        "description": "Crème premium peaux sensibles, acide hyaluronique, 50ml, dermatologiquement testée",
        "price": Decimal("44.99"),
        "stock": 100,
        "category": "Beauté & Santé"
    },
    {
        "name": "Shampooing Cheveux Bouclés",
        "description": "Shampooing spécialisé, sans silicone, 250ml, fortifie et hydrate",
        "price": Decimal("19.99"),
        "stock": 80,
        "category": "Beauté & Santé"
    },
    {
        "name": "Brosse à Dents Électrique",
        "description": "Brosse 5000 oscillations/min, batterie 15 jours, capteur de pression, 3 modes",
        "price": Decimal("69.99"),
        "stock": 40,
        "category": "Beauté & Santé"
    },
    {
        "name": "Supplément Vitamine D3",
        "description": "Vitamines D3 2000 IU, 120 capsules, absorption optimale, 100% naturel",
        "price": Decimal("24.99"),
        "stock": 150,
        "category": "Beauté & Santé"
    },
    
    # Livres
    {
        "name": "Python pour Débutants",
        "description": "Guide complet apprentissage Python, 300 pages, exercices pratiques inclus",
        "price": Decimal("34.99"),
        "stock": 60,
        "category": "Livres"
    },
    {
        "name": "Le Hobbit - Tolkien",
        "description": "Roman fantastique classique, édition brochée, 310 pages, traduction française",
        "price": Decimal("16.99"),
        "stock": 100,
        "category": "Livres"
    },
    {
        "name": "Développement Web Moderne",
        "description": "Maîtrisez React, Vue.js et Angular, 450 pages, exemples réels",
        "price": Decimal("49.99"),
        "stock": 35,
        "category": "Livres"
    },
    {
        "name": "Psychologie des Couleurs",
        "description": "Guide expert utilisation des couleurs, 280 pages, illustrations haute qualité",
        "price": Decimal("39.99"),
        "stock": 25,
        "category": "Livres"
    },
]

# Add products to database
for prod_data in products_data:
    category = categories[prod_data.pop("category")]
    product = Product.objects.create(**prod_data, category=category)
    print(f"✓ Produit créé: {product.name} - {product.price}€")

print("\n" + "="*50)
print("✅ BASE DE DONNÉES REMPLIE AVEC SUCCÈS!")
print("="*50)
print(f"✓ {len(categories)} catégories créées")
print(f"✓ {len(products_data)} produits créés")
