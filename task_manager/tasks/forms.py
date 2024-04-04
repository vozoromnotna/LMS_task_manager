from django import forms
from django.forms import ModelForm
from .models import Project, Task

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    email = forms.EmailField(label="Электронная почта")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "assignee"]