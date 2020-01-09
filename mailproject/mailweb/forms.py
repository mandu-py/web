from django import forms
from .models import Remote

class RemoteForm(forms.Form):
    idx = forms.IntegerField(label='idx')
    system_text = forms.CharField(label='system_text',max_length=200)
    