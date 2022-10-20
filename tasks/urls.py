from django.urls import path
from .views import list_tasks, create_tasks, delete_tasks

urlpatterns = [
    path('', list_tasks),
    path('new_tasks/', create_tasks, name="create_task"),
    path('delete/<int:task_id>/', delete_tasks, name="delete_task")
]