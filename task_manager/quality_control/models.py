from django.db import models
from django.forms import ValidationError
from tasks.models import Project, Task
from django.core.validators import MaxValueValidator, MinValueValidator

class BugReport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name="project_report",
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name="task_report",
        null=True,
        on_delete=models.SET_NULL
    )
    STATUS_CHOICES = { "New":"Новая", "In_pogress": "В работе", "Completed":"Завершена" }
    status = models.CharField(choices=STATUS_CHOICES, default="New", max_length=50)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.task and self.project != self.task.project:
            raise ValidationError("Задача должна относиться к выбранному проекту")

class FeatureRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name="project_feature",
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        null=True,
        related_name="task_feature",
        on_delete=models.SET_NULL
    )
    STATUS_CHOICES = { "Under_consideration":"Рассматривается", "Accepted": "Принята", "Rejected":"Отклонена" }
    status = models.CharField(choices=STATUS_CHOICES, default="Under_consideration", max_length=50)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.task and self.project != self.task.project:
            raise ValidationError("Задача должна относиться к выбранному проекту")
