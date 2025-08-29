from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Tag
from .forms import TaskCreateForm
from django.urls import reverse_lazy


class IndexView(LoginRequiredMixin,ListView):
    template_name = "todo/index.html"
    model = Task
    context_object_name = "task_list"
    ordering = ['done', '-created_at']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('done', '-created_at')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('index')
    template_name = "todo/task_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)