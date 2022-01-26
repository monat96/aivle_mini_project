from django import forms
from .models import Board

class BoardWriteForm(forms.ModelForm):
    
    class Meta:
        model = Board
        fields = ('title','content', 'image')