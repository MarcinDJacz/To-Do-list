from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Tag
from .forms import TaskCreateForm, TagCreateForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .mixins import ConfirmDeleteMixin

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
    success_url = reverse_lazy('todo:index')
    template_name = "todo/task_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.done = not task.done
        task.save()
    return redirect('todo:index')


class TagsListView(LoginRequiredMixin, ListView):
    template_name = "todo/tags_list.html"
    model = Tag
    context_object_name = "tags_list"


class TagCreateView(LoginRequiredMixin, CreateView):
    form_class = TagCreateForm
    success_url = reverse_lazy('todo:tags_list')
    template_name = "todo/tag_create_form.html"


class TaskDeleteView(ConfirmDeleteMixin, LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:index')


class TagDeleteView(ConfirmDeleteMixin, LoginRequiredMixin, DeleteView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('todo:tags_list')