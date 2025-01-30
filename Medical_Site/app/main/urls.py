from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('registration/', views.registration, name='registration'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/edit/<int:pk>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
]