from django.contrib import admin
from .models import Log,Maildata,Userinfo

# Register your models here.

admin.site.register(Log)
admin.site.register(Maildata)
admin.site.register(Userinfo)
