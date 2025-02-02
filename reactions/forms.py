from django import forms
from .models import Scores


class ScoresForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = ('score',)
