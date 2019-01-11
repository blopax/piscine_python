from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='ex02_form'),
]
