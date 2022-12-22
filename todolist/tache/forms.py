from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    description = forms.CharField(
        max_length=255, required=True, widget=forms.TextInput(attrs={
            'placeholder': 'Enter your Task',
            # 'class': 'form-control form-control-lg'
        }))

    class Meta:
        model = Task
        fields = ['description', ]
