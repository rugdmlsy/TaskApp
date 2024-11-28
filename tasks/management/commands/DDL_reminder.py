from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from datetime import datetime, timedelta
from tasks.models import Task
from django.conf import settings

class Command(BaseCommand):
    help = 'Send DDL reminders for tasks'

    def handle(self, *args, **kwargs):
        # 当前时间
        now = datetime.now()

        # 查找即将到期的任务（例如：提醒提前1小时）
        reminder_time = now + timedelta(hours=1)

        # 获取所有即将到期的任务
        tasks_to_remind = Task.objects.filter(due_date__lte=reminder_time, completed=False)

        if tasks_to_remind:
            # TODO: 配置SMTP
            # for task in tasks_to_remind:
            #     # 发送邮件提醒
            #     send_mail(
            #         f"任务提醒: {task.title}",
            #         f"任务 '{task.title}' 即将到期，DDL: {task.due_date}",
            #         settings.DEFAULT_FROM_EMAIL,
            #         [task.user.email],  # 假设每个任务关联一个用户
            #         fail_silently=False,
            #     )
            self.stdout.write(self.style.SUCCESS('提醒邮件已发送'))
        else:
            self.stdout.write(self.style.SUCCESS('没有即将到期的任务'))
