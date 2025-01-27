from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.timezone import now
# from django.core.management.base import BaseCommand


User = get_user_model()




# Create your models here.

from django.db import models
from django.utils import timezone


class StatusChoices(models.TextChoices):
    TO_DO = ('to_do', 'To Do')
    IN_PROGRESS = ('in_progress', 'In Progress')
    COMPLETED = ('completed', 'Completed')

class PriorityChoices(models.TextChoices):
    LOW = ('low', 'Low')
    MEDIUM = ('medium', 'Medium')
    HIGH = ('high', 'High')



class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100 , blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=12, choices=StatusChoices.choices, default=StatusChoices.TO_DO)
    priority = models.CharField(max_length=6, choices=PriorityChoices.choices, default=PriorityChoices.LOW)

    def __str__(self):
        return f" {self.title}"
    
# class Command(BaseCommand):
    # help = 'Delete tasks that are overdue for more than 7 days'

    # def handle(self, *args, **kwargs):
    #     cuttoff_time = timezone.now() - timedelta(days=7)
    #     overdue_tasks = Task.objects.filter(due_date__lt=cuttoff_time, completed=False)
    #     deleted_count, _ = overdue_tasks.delete()
    #     if deleted_count:
    #         self.stdout.write(self.style.SUCCESS(f'successfully deleted {deleted_count} overdue tasks'))




    @property
    def is_overdue_and_incomplete(self):
        """Check if the task is overdue and incomplete."""
        return self.status != 'completed' and timezone.now() > self.due_date

    
