from django import forms
from .models import Remote

class RemoteForm(forms.ModelForm):
    class Meta:
        model = Remote
        fields = ('idx','start_time','end_time','local_ip','remote_ip','system_text',)