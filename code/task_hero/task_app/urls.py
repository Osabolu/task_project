from django.urls import path
from . import views


app_name = "task_app"

urlpatterns = [
    path("home/", views.home, name="home"),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('confirm-delete/<int:task_id>/', views.confirm_delete_task, name='confirm_delete_task'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
   
]