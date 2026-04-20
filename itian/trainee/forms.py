from django import forms
from .model import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model=Trainee
        fields=['name','age','course']