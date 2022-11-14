from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from todo.models import Tag


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
