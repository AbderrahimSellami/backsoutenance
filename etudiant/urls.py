from django.urls import path
from . import views


urlpatterns = [
    path('', views.etudiant, name='etudiant'),
    path('liste_themes/', views.liste_themes, name='liste_themes'),
]