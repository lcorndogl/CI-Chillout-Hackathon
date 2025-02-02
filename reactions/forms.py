from django import forms
from .models import Score


class ScoresForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('score',)
