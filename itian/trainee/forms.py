from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model=Trainee
        fields=['name','age','course']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
            'course': forms.SelectMultiple(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
        }
    def clean_age(self):
        age=self.cleaned_data.get('age')
        if age < 21:
            raise forms.ValidationError('minimum age is 15')
        return age
    
        