# Projet E-commerce Django

## Description du projet

Ce projet est une application web e-commerce développée avec Django. L'objectif est de construire une boutique en ligne simple qui permet d'afficher des produits, de les organiser par catégories, de consulter le détail d'un produit, d'ajouter des articles au panier, de gérer une liste de favoris et de créer un compte utilisateur.

Le projet suit l'architecture MVT de Django :

- **Model** : définition des données avec les modèles `Product` et `Category`.
- **View** : logique de traitement dans les fichiers `views.py`.
- **Template** : affichage HTML avec Bootstrap dans les fichiers du dossier `templates`.

## Fonctionnalités principales

- Affichage de la liste des produits.
- Recherche de produits par nom ou description.
- Filtrage des produits par catégorie.
- Tri des produits par nouveauté ou par prix.
- Page de détail pour chaque produit.
- Gestion des catégories.
- Ajout et suppression de produits dans le panier.
- Ajout et suppression de produits dans les favoris.
- Inscription utilisateur avec le système d'authentification Django.
- Page profil protégée par connexion.
- Interface d'administration Django pour gérer les produits et les catégories.
- Gestion des images des produits avec `MEDIA_URL`, `MEDIA_ROOT` et Pillow.
- Base de données MySQL configurable avec variables d'environnement.
- Service MySQL disponible avec Docker Compose.

## Technologies utilisées

- Python
- Django 4.2.11
- MySQL
- mysqlclient
- Pillow
- Bootstrap
- Docker Compose

Les dépendances du projet sont listées dans le fichier `requirements.txt`.

## Structure du projet

```text
ecommerce/
|-- manage.py
|-- requirements.txt
|-- docker-compose.yaml
|-- README.md
|-- ecommerce/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- products/
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   |-- admin.py
|   |-- migrations/
|   `-- templates/products/
|-- accounts/
|   |-- forms.py
|   |-- views.py
|   |-- urls.py
|   `-- templates/registration/
|-- templates/
|   `-- layout.html
`-- images/
    `-- products/
```

## Applications du projet

### Application `products`

L'application `products` contient toute la logique liée à la boutique.

Elle gère :

- les produits ;
- les catégories ;
- la liste des produits ;
- le détail d'un produit ;
- le panier ;
- les favoris ;
- les pages de catégories.

Les modèles principaux sont :

### `Category`

Le modèle `Category` permet de classer les produits. Il contient :

- `name` : nom de la catégorie ;
- `created_at` : date de création.

### `Product`

Le modèle `Product` représente un produit de la boutique. Il contient :

- `name` : nom du produit ;
- `description` : description du produit ;
- `price` : prix ;
- `stock` : quantité disponible ;
- `image` : image du produit ;
- `category` : catégorie liée au produit ;
- `created_at` : date de création.

La relation entre `Product` et `Category` est une relation plusieurs-vers-un avec `ForeignKey`. Une catégorie peut donc contenir plusieurs produits.

### Application `accounts`

L'application `accounts` gère la partie utilisateur.

Elle contient :

- un formulaire d'inscription basé sur `UserCreationForm` ;
- une vue `signup` pour créer un compte ;
- une vue `profile` accessible seulement aux utilisateurs connectés ;
- une redirection automatique vers le profil si l'utilisateur est déjà connecté.

Django fournit aussi les routes d'authentification standard avec `django.contrib.auth.urls`, comme la connexion et la déconnexion.

## Routage

Le fichier principal `ecommerce/urls.py` configure les routes globales :

- `/admin/` : interface d'administration Django ;
- `/` : redirection vers la liste des produits ;
- `/products/` : routes de l'application produits ;
- `/accounts/` : routes de l'application comptes ;
- `/auth/` : routes d'authentification Django.

Les routes principales de `products` sont :

- `/products/` : liste des produits ;
- `/products/<id>/` : détail d'un produit ;
- `/products/cart/` : panier ;
- `/products/cart/add/<id>/` : ajout au panier ;
- `/products/cart/remove/<id>/` : suppression du panier ;
- `/products/favorites/` : favoris ;
- `/products/favorites/add/<id>/` : ajout aux favoris ;
- `/products/favorites/remove/<id>/` : suppression des favoris ;
- `/products/categories/` : liste des catégories ;
- `/products/categories/<id>/` : détail d'une catégorie.

Les routes principales de `accounts` sont :

- `/accounts/` : redirection selon l'état de connexion ;
- `/accounts/signup/` : inscription ;
- `/accounts/profile/` : profil utilisateur.

## Base de données

Le projet utilise MySQL comme base de données.

Dans `settings.py`, la configuration utilise des variables d'environnement :

- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_HOST`
- `MYSQL_PORT`

Si ces variables ne sont pas définies, Django utilise les valeurs par défaut suivantes :

- base : `db_ecommerce`
- utilisateur : `root`
- mot de passe : vide
- hôte : `127.0.0.1`
- port : `3306`

Le fichier `docker-compose.yaml` permet de lancer un conteneur MySQL avec :

- image : `mysql`
- conteneur : `mysql-db`
- base créée : `DB_ECOMMERCE`
- port exposé : `3306`
- volume persistant : `db_data`

## Comment j'ai construit l'application

### 1. Création du projet Django

J'ai commencé par créer un projet Django nommé `ecommerce`. Le fichier `manage.py` sert de point d'entrée pour lancer les commandes Django, tandis que le dossier `ecommerce/` contient la configuration principale du projet.

### 2. Création de l'application `products`

J'ai ensuite créé l'application `products` pour séparer la logique de la boutique du reste du projet. Cette application contient les modèles, les vues, les routes et les templates liés aux produits.

Après sa création, je l'ai ajoutée dans `INSTALLED_APPS` dans `settings.py`.

### 3. Création des modèles

J'ai défini deux modèles dans `products/models.py` :

- `Category` pour les catégories ;
- `Product` pour les produits.

Le modèle `Product` est relié à `Category` avec une clé étrangère. J'ai ensuite généré et appliqué les migrations avec les commandes Django.

### 4. Configuration de l'administration

Dans `products/admin.py`, j'ai enregistré les modèles `Product` et `Category` pour pouvoir les gérer depuis l'interface d'administration Django.

J'ai aussi personnalisé l'affichage avec :

- `list_display`
- `list_filter`
- `search_fields`

### 5. Création des vues et des templates

J'ai créé les vues dans `products/views.py` pour afficher les données venant de la base :

- liste des produits ;
- détail d'un produit ;
- liste des catégories ;
- détail d'une catégorie ;
- panier ;
- favoris.

Les pages HTML sont placées dans `products/templates/products/`. Le fichier global `templates/layout.html` sert de base commune pour les pages.

### 6. Ajout de la recherche, des filtres et du tri

Dans la vue `product_list`, j'ai ajouté :

- une recherche avec `Q` pour chercher dans le nom et la description ;
- un filtre par catégorie ;
- un tri par prix ou par date de création.

### 7. Gestion du panier et des favoris

Le panier et les favoris sont stockés dans la session Django. Cela permet de garder les produits sélectionnés par l'utilisateur pendant sa navigation, sans créer de modèles supplémentaires.

### 8. Gestion des images

J'ai ajouté un champ `ImageField` dans le modèle `Product`. Les images sont enregistrées dans le dossier `images/products/`.

Dans `settings.py`, j'ai configuré :

- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'images'`

Dans `ecommerce/urls.py`, j'ai ajouté la configuration nécessaire pour servir les fichiers médias en mode développement.

### 9. Création de l'application `accounts`

J'ai créé l'application `accounts` pour gérer l'inscription et le profil utilisateur.

Le formulaire `RegisterForm` hérite de `UserCreationForm` et ajoute un champ email. Après inscription, l'utilisateur est automatiquement connecté et redirigé vers son profil.

### 10. Configuration de MySQL et Docker

J'ai configuré Django pour utiliser MySQL dans `settings.py`. Le fichier `docker-compose.yaml` permet de lancer rapidement un serveur MySQL local avec Docker.

## Installation et lancement

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 2. Activer l'environnement virtuel

Sur Windows :

```bash
.venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer MySQL avec Docker

```bash
docker compose up -d
```

### 5. Configurer les variables d'environnement

Exemple avec PowerShell :

```powershell
$env:MYSQL_DATABASE="DB_ECOMMERCE"
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="root"
$env:MYSQL_HOST="127.0.0.1"
$env:MYSQL_PORT="3306"
```

### 6. Appliquer les migrations

```bash
python manage.py migrate
```

### 7. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 8. Lancer le serveur Django

```bash
python manage.py runserver
```

Le site est ensuite disponible à l'adresse :

```text
http://127.0.0.1:8000/
```

## Commandes utiles

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py check
```

## Remarques

- Le dossier `images/` contient les images des produits.
- Les fichiers de cache Python et les environnements virtuels ne doivent pas être suivis par Git.
- Le fichier `.gitignore` ignore les fichiers générés comme `__pycache__`, les bases locales et les environnements virtuels.
- Le projet utilise les sessions Django pour le panier et les favoris.
