from django import forms
from .models import Board

class BoardWriteForm(forms.ModelForm):
    upload = forms.ImageField(label='첨부 파일', required=False, 
        widget=forms.FileInput(attrs={'class': 'form'}))
    class Meta:
        model = Board
        fields = ('title','content', 'image')