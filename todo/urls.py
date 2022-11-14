from django.urls import path

from todo.views import TagListView, TagCreateView

urlpatterns = [
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/crate?",
        TagCreateView.as_view(),
        name="tag-create"
    ),
]
