from django.urls import path, include
from . import views

urlpatterns = [

    path('get_planning/', views.get_planning, name='get_planning'),
    path('add_theme/', views.add_theme, name='add_theme'),
    path('delete_theme/', views.delete_theme, name='delete_theme'),
    path('plateforme/',views.plateforme, name='plateforme'),
]