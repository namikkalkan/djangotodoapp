
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path ('',views.index),
    path('addTodo',views.addTodo),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('api/',views.api),
    path('api/tasks', views.api),
    path('api/tasks/<int:id>', views.api1),

]

'''
    path('tasks/', views.main_api),
    path('tasks/<str:pk>/', views.main_api),
    path('tasks/', views.main_api),
    path('tasks/<str:pk>/', views.main_api),
'''
