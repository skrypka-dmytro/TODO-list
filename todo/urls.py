from django.urls import path

from todo.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, task_status

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasls/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasls/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasls/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasls/<int:pk>/<status>/delete/",
        task_status,
        name="task-status"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todo"
