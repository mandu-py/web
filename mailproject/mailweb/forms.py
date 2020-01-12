from django import forms
from .models import Remote,RemoteLocal,RemoteUser

class RemoteForm(forms.ModelForm):
    class Meta:
        model = Remote
        fields = ('idx','start_time','end_time','local_ip','remote_ip','system_text',)


class RemoteLocalForm(forms.ModelForm):
    class Meta:
        model = RemoteLocal
        fields = ('idx','user_ip','user_name',)


class RemoteUserForm(forms.ModelForm):
    class Meta:
        model = RemoteUser
        fields = ('idx','user_ip','user_name','user_system',)
