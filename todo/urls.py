from django.urls import path

from todo.views import (TaskCreateView,
                        TagCreateView,
                        TaskUpdateView,
                        TagUpdateView,
                        TagsListView,
                        IndexView,
                        task_done,
                        TaskDeleteView,
                        TagDeleteView)

app_name = "todo"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("new_task/", TaskCreateView.as_view(), name="create_task"),
    path('task_done/<int:pk>', task_done, name='task_done'),
    path('tags/', TagsListView.as_view(), name='tags_list'),
    path('new_tag/', TagCreateView.as_view(), name='create_tag'),
    path("task/<int:pk>/delete/",
         TaskDeleteView.as_view(), name='task_delete'),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(), name='tag_delete'),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(), name='task_update'),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(), name='tag_update'),
]
