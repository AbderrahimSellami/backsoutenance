from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentification/',include('authentification.urls'),name='authentification'),
    path('planning/',include('planning.urls'),name='planning'),
    path('utilisateurs/',include('utilisateurs.urls'),name='utilisateurs'),
    path('enseignant/',include('enseignant.urls'),name='enseignant'),
    path('etudiant/',include('etudiant.urls'),name='etudiant'),

]
