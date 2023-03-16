from django import forms
from .models import cinema


class Movieform(forms.ModelForm):
    class Meta:
        model=cinema
        fields=['name1','budget2','desc3','img4']