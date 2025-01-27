from django import forms
from .models import Task
from django.utils import timezone



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


# class TaskManualForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(max_length=255)
#     due_date = forms.DateTimeField()
#     status = forms.ChoiceField()
#     priority = forms.ChoiceField()