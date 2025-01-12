from django import forms
from .models import game

class myForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ['user_input', 'difficulty'] 