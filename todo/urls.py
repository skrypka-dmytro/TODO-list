from django.urls import path

from todo.views import TagListView, TagCreateView, TagUpdateView

urlpatterns = [
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/crate/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
]
