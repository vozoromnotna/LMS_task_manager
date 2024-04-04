from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from .models import Project, Task
from .forms import FeedbackForm, ProjectForm, TaskForm

def another_page(requset):
    return HttpResponse('Это другая страница приложения tasks')


class IndexView(TemplateView):
    template_name = 'tasks/index.html'
    
    
class ProjectsListView(ListView):
    model = Project
    context_object_name = 'projects_list'
    template_name = 'tasks/projects_list.html'

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

class TaskDetaiView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

class FeedbackView(FormView):
    form_class = FeedbackForm
    success_url = reverse_lazy('tasks:index')
    template_name = "tasks/feedback.html"

class CreatProjectView(CreateView):
    form_class = ProjectForm
    success_url = reverse_lazy('tasks:projects_list')
    template_name = "tasks/project_create.html"

class AddTaskView(CreateView):
    form_class = TaskForm
    pk_url_kwarg = 'task_id'
    template_name = "tasks/add_task.html"
    def form_valid(self, form: TaskForm) -> HttpResponse:
        task = form.instance
        project = get_object_or_404(Project, pk=self.kwargs["project_id"])
        task.project = project
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse("tasks:project_detail", kwargs={"project_id": self.kwargs["project_id"]})
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    pk_url_kwarg = "project_id"
    success_url = reverse_lazy('tasks:projects_list')
    template_name = "tasks/project_update.html"
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_update.html"
    pk_url_kwarg = 'task_id'
    
    def get_success_url(self) -> str:
        project_id = self.object.project.id
        task_id = self.object.id
        
        return reverse_lazy("tasks:task_detail", kwargs={"project_id": project_id, "task_id": task_id})
    
class ProjectDeleteView(DeleteView):
    model = Project
    pk_url_kwarg = "project_id"
    success_url = reverse_lazy('tasks:projects_list')
    template_name="tasks/project_confirm_delete.html"
    
class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = "task_id"
    template_name="tasks/task_confirm_delete.html"
    
    def get_success_url(self) -> str:
        return reverse("tasks:project_detail", kwargs={"project_id": self.kwargs["project_id"]})
        