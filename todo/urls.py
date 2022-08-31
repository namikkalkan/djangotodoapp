
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path ('',views.index),
    path('addTodo',views.addTodo),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('api/',views.api),
    path('api_tasks/', views.task_api),
    path('api_create_task/', views.task_create_api),
    path('api_update_task/<str:pk>/', views.task_update_api),
    path('api_delete_task/<str:pk>/', views.task_delete_api),

    ]