from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirige la racine du site vers la liste des produits
    path('', RedirectView.as_view(pattern_name='product_list', permanent=False)),
    
    # URLs de l'application products
    path('products/', include('products.urls')),
    
    # URLs de l'application accounts (inscription, profil)
    path('accounts/', include('accounts.urls')),
    
    # URLs d'authentification fournies par Django (login, logout, password reset...)
    path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)