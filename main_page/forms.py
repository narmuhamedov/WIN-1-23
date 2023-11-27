from django import forms
from . import models

class FilmForm(forms.ModelForm):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'