# Generated by Django 5.0.2 on 2024-03-25 18:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'Новая'), ('In_pogress', 'В работе'), ('Completed', 'Завершена')], default='New', max_length=50)),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_report', to='tasks.project')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_report', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Under_consideration', 'Рассматривается'), ('Accepted', 'Принята'), ('Rejected', 'Отклонена')], default='Under_consideration', max_length=50)),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_feature', to='tasks.project')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_feature', to='tasks.task')),
            ],
        ),
    ]