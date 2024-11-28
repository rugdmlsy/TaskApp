from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()  # DDL 时间
    completed = models.BooleanField(default=False)  # 任务是否完成
    tags = models.ManyToManyField(Tag, related_name='tasks')  # 多对多关系
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
        return self.title
