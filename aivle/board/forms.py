from django import forms
from .models import Board

class WritingForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title','content')