from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=65)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    work_status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content} (created: {self.datetime})"
