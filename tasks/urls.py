from django.urls import path
from django_cron import CronJobBase, Schedule
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # 任务列表
    path('task/add/', views.add_task, name='add_task'),  # 任务添加页面
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # 任务详情
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),  # 任务编辑页面
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),  # 删除任务
    path('tag/<int:tag_id>/', views.task_by_tag, name='task_by_tag'),
]

