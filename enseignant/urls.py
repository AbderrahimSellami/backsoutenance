# Dans urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.enseignant, name='enseignant'),
    path('nondispo/', views.nondispo, name='nondispo'),
    path('binomes/', views.binomes, name='binomes'),
    path('nondispo/<int:id>/', views.delete_non_dispo, name='delete_non_dispo'),
    path('add-non-dispo/', views.add_non_dispo, name='add_non_dispo'),
    path('liste-themes/', views.liste_themes, name='liste_themes'),
    path('modifier-theme/<int:id>/', views.update_theme, name='update_theme'),
    path('supprimer-theme/<int:id>/', views.delete_theme, name='delete_theme'),
    path('proposer_theme/', views.proposer_theme, name='proposer_theme'),
]

