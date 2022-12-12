from .models import place
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=place
        fields=['name','desc','img','price']