# Projet E-Commerce Django

## Description
Application web e-commerce développée avec le framework Django dans le cadre du cours
Développement Web Python 2026 (Mr. BOUSSELHAM).
Le projet couvre la mise en place d'une architecture MVT complète avec gestion
des produits, catégories, base de données et interface d'administration.

---

## Atelier 1 — Introduction à Django et architecture MVT

Cet atelier introduit le framework Django et son architecture MVT (Model-View-Template).
Il couvre la mise en place de l'environnement de développement, la création du projet
`ecommerce` et de l'application `products`, la configuration des URLs, la création de
vues simples et les premiers templates HTML.

**Compétences abordées :**
- Installation de Django et création d'un environnement virtuel
- Structure d'un projet Django
- Architecture MVT (Model - View - Template)
- Création de vues et routage URL
- Templates HTML de base

---

## Atelier 2 — Gestion et récupération de données

Cet atelier approfondit l'interaction avec la base de données via l'ORM de Django.
Il couvre la création des modèles `Product` et `Category`, les migrations, les relations
entre modèles (ForeignKey), l'interface d'administration, les templates dynamiques,
la gestion des images avec Pillow, et la connexion à MySQL.

**Compétences abordées :**
- Modèles Django et ORM
- Migrations (`makemigrations` / `migrate`)
- Relations entre tables (ForeignKey)
- Interface d'administration Django
- Templates dynamiques (liste & détail)
- Gestion des fichiers médias (Pillow)
- Connexion à une base de données MySQL

---

## Structure du projet

ecommerce_project/
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── products/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── category_list.html
│   │       └── category_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── images/
│   └── products/
├── myenv/
├── db.sqlite3
└── manage.py

---

## Modèles

### Category
| Champ        | Type                          |
|--------------|-------------------------------|
| name         | CharField(max_length=100)     |
| description  | TextField(blank=True)         |
| created_at   | DateTimeField(auto_now_add)   |

### Product
| Champ        | Type                                    |
|--------------|-----------------------------------------|
| name         | CharField(max_length=255)               |
| description  | TextField                               |
| price        | DecimalField(max_digits=10, decimals=2) |
| stock        | PositiveIntegerField                    |
| image        | ImageField(upload_to='products/images') |
| category     | ForeignKey(Category)                    |
| created_at   | DateTimeField(auto_now_add)             |

---

## URLs disponibles

| URL                        | Vue             | Nom             |
|----------------------------|-----------------|-----------------|
| /products/                 | product_list    | product_list    |
| /products/<int:id>/        | product_detail  | product_detail  |
| /products/categories/      | category_list   | category_list   |
| /products/category/<id>/   | category_detail | category_detail |

---

## Installation

1. Cloner le projet et entrer dans le dossier

    cd ecommerce_project

2. Créer et activer l'environnement virtuel

    virtualenv myenv
    myenv\scripts\activate

3. Installer les dépendances

    pip install django
    pip install pillow
    pip install mysqlclient

4. Appliquer les migrations

    python manage.py makemigrations
    python manage.py migrate

5. Créer un super utilisateur

    python manage.py createsuperuser

6. Lancer le serveur

    python manage.py runserver

---

## Configuration MySQL (optionnel)

Dans settings.py, remplacer la configuration DATABASES par :

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_ecommerce',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

---

## Configuration des médias

Dans settings.py :

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'images')

---

## Accès

| Page            | URL                             |
|-----------------|---------------------------------|
| Liste produits  | http://127.0.0.1:8000/products/ |
| Interface admin | http://127.0.0.1:8000/admin/    |

---

## Technologies utilisées

- Python 3.x
- Django
- SQLite3 / MySQL
- Pillow
- HTML / Django Template Language