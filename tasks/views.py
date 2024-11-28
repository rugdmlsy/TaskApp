from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task, Tag
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tags = Tag.objects.all()  # 获取所有标签
    tasks = Task.objects.all().order_by('due_date')  # 获取所有任务，按DDL时间排序
    return render(request, 'tasks/task_list.html', {'tags': tags, 'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # 保存新任务
            return redirect('task_list')  # 添加成功后重定向到任务列表页面
    else:
        form = TaskForm()  # GET 请求时显示空表单

    return render(request, 'tasks/add_task.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()  # 删除任务
    return redirect('task_list')  # 删除后重定向到任务列表


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)  # 获取指定 ID 的任务
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # 用现有任务填充表单
        if form.is_valid():
            form.save()  # 保存修改
            return redirect('task_list')  # 编辑成功后重定向到任务列表
    else:
        form = TaskForm(instance=task)  # GET 请求时显示现有任务的数据

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


def task_by_tag(request, tag_id):
    # 获取标签对象
    tag = Tag.objects.get(id=tag_id)

    # 获取该标签下的所有任务
    tasks = tag.tasks.all()  # 通过 related_name 获取所有关联的任务

    return render(request, 'tasks/task_by_tag.html', {'tag': tag, 'tasks': tasks})
