from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.utilisateurs, name='utilisateurs'),
    path('comptes/',views.comptes, name='comptes'),
    path('ajout_user/',views.ajout_user , name='ajout_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('soutenance/',views.soutenance , name='soutenance'),
]