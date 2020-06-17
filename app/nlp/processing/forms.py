from django import forms
from django.forms import ClearableFileInput

from .models import InputData, Resume


class TextForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['text']


class UploadResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume']

