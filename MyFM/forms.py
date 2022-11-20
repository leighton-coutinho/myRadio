from django import forms
from django.forms import ModelForm
from .models import Recording

class RecordingForm(ModelForm):
    class Meta:
        model = Recording
        fields = "__all__"
        