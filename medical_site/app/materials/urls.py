from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('<int:pk>/', views.material_detail, name='material_detail'),
    path('create/', views.material_create, name='material_create'),
    path('<int:pk>/update/', views.material_update, name='material_update'),
    path('<int:pk>/delete/', views.material_delete, name='material_delete'),
]