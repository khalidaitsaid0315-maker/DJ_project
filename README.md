# Projet E-commerce Django - DJ_project

## Description
[cite_start]Ce projet a été développé au cours de deux ateliers pratiques portant sur le framework Django[cite: 257, 2]. [cite_start]Il met en œuvre une application de gestion de produits et de catégories en utilisant l'architecture MVT (Model-View-Template)[cite: 278].

---

##  Atelier 1 : Fondamentaux et Configuration
L'objectif de cet atelier était de mettre en place l'environnement de développement et de comprendre le flux de base (URL -> Vue -> Template).

### [cite_start]1. Préparation de l'Environnement [cite: 298-314]
* [cite_start]**Installation des outils** : Mise à jour de `pip` et installation de `virtualenv`[cite: 300, 303].
* [cite_start]**Environnement virtuel** : Création du répertoire `ecommerce_project` et activation de l'environnement virtuel `myenv`[cite: 305, 309, 312].
* [cite_start]**Installation de Django** : Installation du framework via la commande `pip install django`[cite: 314].

### [cite_start]2. Initialisation du Projet [cite: 315-346]
* [cite_start]**Création du projet** : Génération de la structure de base nommée `ecommerce`[cite: 317].
* [cite_start]**Vérification** : Test du bon fonctionnement avec le serveur de développement (`python manage.py runserver`)[cite: 340].
* [cite_start]**Structure** : Compréhension des fichiers clés tels que `settings.py` (configuration), `urls.py` (routage) et `manage.py` (point d'entrée) [cite: 334-337].

### [cite_start]3. Création de l'Application [cite: 349-386]
* [cite_start]**Initialisation** : Création de l'application `products` pour gérer la logique métier des articles[cite: 353].
* [cite_start]**Configuration** : Déclaration de l'application dans la liste `INSTALLED_APPS` du fichier `settings.py`[cite: 374, 383].

### [cite_start]4. Vues et Routage Initiaux [cite: 389-447]
* [cite_start]**Vues** : Création des fonctions `product_list` et `product_detail` dans `views.py` pour rendre les templates [cite: 391-395].
* [cite_start]**Routage** : Configuration des fichiers `urls.py` au niveau du projet et de l'application pour mapper les adresses[cite: 396, 403].
* [cite_start]**Templates** : Création d'un dossier `templates` et des premiers fichiers HTML pour valider l'affichage[cite: 410, 427, 430].

---

##  Atelier 2 : Modélisation et Persistance des Données
Cet atelier s'est concentré sur l'interaction avec les bases de données via l'ORM de Django, la gestion des médias et l'utilisation de MySQL.

### [cite_start]1. Modélisation et ORM [cite: 3-28]
* [cite_start]**Modèle Product** : Définition des attributs (nom, prix, image, stock) dans `models.py` [cite: 19, 22-26].
* [cite_start]**Modèle Category** : Création d'un modèle pour classer les articles[cite: 44, 54].
* [cite_start]**Relations** : Mise en place d'une relation plusieurs-à-un (`ForeignKey`) entre les produits et les catégories[cite: 49, 68, 70].

### [cite_start]2. Migrations [cite: 29-42, 73-77]
* [cite_start]**Préparation** : Utilisation de `makemigrations` pour générer les fichiers de modification[cite: 33, 74].
* [cite_start]**Application** : Synchronisation avec la base de données via la commande `migrate`[cite: 39, 76].

### [cite_start]3. Interface d'Administration [cite: 78-89]
* [cite_start]**Enregistrement** : Ajout des modèles `Category` et `Product` dans `admin.py`[cite: 82].
* [cite_start]**Personnalisation** : Utilisation des décorateurs `@admin.register` et configuration de l'affichage avec `list_display`, `list_filter` et `search_fields` [cite: 83, 85-89].

### [cite_start]4. Logique Métier et Templates Dynamiques [cite: 90-176]
* [cite_start]**Récupération des données** : Utilisation de `Product.objects.all()` et `get_object_or_484` pour extraire les données[cite: 96, 99].
* [cite_start]**Accès aux relations** : Exploitation de `related_name='products'` pour lister les produits d'une catégorie spécifique[cite: 107].
* [cite_start]**Affichage** : Utilisation de boucles `{% for %}` et de variables de template pour un affichage dynamique[cite: 130, 150, 164, 171].

### [cite_start]5. Gestion des Images [cite: 177-217]
* [cite_start]**Dépendance** : Installation de la bibliothèque `Pillow`[cite: 180].
* [cite_start]**Configuration** : Définition de `MEDIA_URL` et `MEDIA_ROOT` dans `settings.py` pour stocker les fichiers sur le serveur [cite: 194-203].
* [cite_start]**Routage média** : Ajout de la configuration statique dans `urls.py` principal[cite: 211, 217].

### [cite_start]6. Connexion à MySQL [cite: 222-254]
* [cite_start]**Base de données** : Création de la base `db_ecommerce` via phpMyAdmin (XAMPP/Wampserver)[cite: 226, 227].
* [cite_start]**Configuration Django** : Modification du dictionnaire `DATABASES` pour pointer vers le moteur MySQL [cite: 228, 231-249].
* [cite_start]**Connecteur** : Installation de `mysqlclient` pour permettre la communication entre Python et MySQL[cite: 251, 252].