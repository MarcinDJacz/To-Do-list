from django.urls import path

from todo.views import TaskCreateView, TagCreateView, TagsListView, IndexView, task_done

app_name = "todo"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("new_task/", TaskCreateView.as_view(), name="create_task"),
    path('task_done/<int:pk>', task_done, name='task_done'),
    path('tags/', TagsListView.as_view(), name='tags_list'),
    path('new_tag/', TagCreateView.as_view(), name='create_tag'),

]

