from django.urls import path
from .views import create_task, update_task, delete_task


# app_name = 'tache'


urlpatterns = [
    path("task/", create_task, name='task'),
    path('<int:pk>/update/', update_task, name='update'),
    path('<int:pk>/delete/', delete_task, name='delete'),
]
