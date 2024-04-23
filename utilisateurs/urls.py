from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.utilisateurs, name='utilisateurs'),
    path('comptes/',views.comptes, name='comptes'),
]