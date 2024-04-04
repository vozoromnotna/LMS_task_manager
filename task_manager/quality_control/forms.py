from django.forms import ModelForm
from django import forms
from tasks.models import Task, Project 
from .models import *

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']
        labels = {'title': 'Название', 'description': 'Описание', 'status': 'Статус', 'priority':'Приоритет', 'project':'Проект', 'task':'Задача'}
        
class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']
        labels = {'title': 'Название', 'description': 'Описание', 'status': 'Статус', 'priority':'Приоритет', 'project':'Проект', 'task':'Задача'}