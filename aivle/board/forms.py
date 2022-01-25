from dataclasses import fields
from django import forms
from .models import *

class BoardWriteForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = [
            'title',
            'contents',
            'user_id'
        ]
