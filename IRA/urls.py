"""Configuration des URLs pour l'application IRA

La liste `urlpatterns` route les URLs vers des vues. Pour plus d'informations, voir :
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Exemples :
Vues basées sur des fonctions
    1. Ajouter une importation :  from my_app import views
    2. Ajouter une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajouter une importation :  from other_app.views import Home
    2. Ajouter une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclusion d'un autre URLconf
    1. Importer la fonction include() : from django.urls import include, path
    2. Ajouter une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guesthouse.urls')),
    
   
]
