from django.urls import path
from . import views

urlpatterns = [
    path('django', views.django, name='ex01_django'),
    path('affichage', views.affichage, name='ex01_affichage'),
    path('templates', views.templates, name='ex01_templates'),
]
