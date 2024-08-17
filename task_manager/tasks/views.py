from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
 model = Task
 template_name = 'tasks/task_confirm_delete.html'
 success_url = reverse_lazy('task_list')

