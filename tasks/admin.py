from django.contrib import admin
from .models import Task, Tag

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'created_at', 'updated_at')  # 在后台展示的字段
    list_filter = ('completed', 'due_date')  # 添加过滤器
    search_fields = ('title', 'description')  # 添加搜索框

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
