from django.urls import path
from . import views
from .views import task_detail

app_name = 'tasks'

urlpatterns = [
    path('gantt/', views.task_gantt, name='task_gantt'),
    path('', views.TaskListView.as_view(), name='task_list'),
    # path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
]