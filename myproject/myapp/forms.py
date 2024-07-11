from django import forms
from .models import Tree

class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['name', 'height', 'image1', 'image2', 'image3']
