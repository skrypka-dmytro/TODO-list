from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


def task_status(request, pk: int, status) -> HttpResponseRedirect:
    task = Task.objects.get(pk=pk)
    if status == "done":
        task.work_status = True
    elif status == "not_done":
        task.work_status = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))

