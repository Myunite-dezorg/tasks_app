from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.DateField()
    is_deadline = models.BooleanField(default=False)
    deadline_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    shared_with = models.ManyToManyField(User, blank=True, related_name='shared_tasks')

    def __str__(self):
        return self.name

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task.name} - {self.name}"