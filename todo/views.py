from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Tag
from .forms import TaskCreateForm
from django.urls import reverse_lazy


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "todo/index.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('todo/index.html')
    template_name = "todo/task_create_form.html"
