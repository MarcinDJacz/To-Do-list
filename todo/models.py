from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    content = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)


