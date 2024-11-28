from datetime import timezone

from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'tags', 'completed']  # 包含要展示的字段

    # 可以根据需要添加自定义验证
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        # if due_date < timezone.now():
        #     raise forms.ValidationError("DDL 时间不能小于当前时间")
        return due_date
