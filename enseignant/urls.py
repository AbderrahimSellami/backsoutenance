from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.enseignant, name='enseignant'),
    path('nondispo/',views.nondispo, name='nondispo'),
    path('binomes/',views.binomes, name='binomes'),
]