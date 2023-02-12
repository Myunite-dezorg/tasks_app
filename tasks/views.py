from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Task, SubTask

def task_gantt(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_gantt.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    subtasks = task.subtasks.all()
    return render(request, 'task/task_detail.html', {'task': task, 'subtasks': subtasks})

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'

class SubTaskListView(ListView):
    model = SubTask
    template_name = 'task/subtask_list.html'
    context_object_name = 'subtasks'

class SubTaskDetailView(DetailView):
    model = SubTask
    template_name = 'task/subtask_detail.html'