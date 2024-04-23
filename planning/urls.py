from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.planning, name='planning'),
    path('get_planning/',views.get_planning, name='get_planning'),
]