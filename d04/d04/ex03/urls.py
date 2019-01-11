from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='ex03_table'),
]
