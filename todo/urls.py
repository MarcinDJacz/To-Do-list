from django.urls import path
from todo.views import TaskCreateView

app_name = "todo"

urlpatterns = [
    path("new_task/", TaskCreateView.as_view(), name="create_task"),
]

