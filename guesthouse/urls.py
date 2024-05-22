from django.urls import path
from django.contrib import admin
from guesthouse import views


urlpatterns = [
    path('', views.home, name='home'),
    path('guesthouse/reservation/', views.reservation, name='reservation'),
    path('guesthouse/payement/', views.payement, name='payement'),
    path('guesthouse/reservation/salle/', views.salle_form_view, name='RessalleForm'),
    path('guesthouse/reservation/liste/', views.liste_attributs, name='liste_attributs'),
    path('guesthouse/reservation/listehebergement/', views.liste_chambre, name='liste_chambre'),
    path('guesthouse/reservation/liste/edit/', views.update, name='update'),
    path('guesthouse/reservation/liste/delete/', views.delete, name='delete'),
    path('guesthouse/reservation/ajoutSalle/', views.salle_view, name='SalleForm'),
    path('guesthouse/reservation/ajoutChambre/', views.hebergement_view, name='HebergementForm'),
    path('guesthouse/connexion/', views.connexion, name='connexion'),
    path('guesthouse/deconnexion/', views.deconnexion, name='deconnexion'),
    path('guesthouse/reservation/hebergement/', views.hebergement_form_view, name='ReshebergementForm'),
    path('guesthouse/reservation/calendrier/', views.calendrier, name='calendrier'),
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),

]