from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.authentification, name='authentification'),
    path('form_submission', views.form_submission , name ='form_submission'),
]