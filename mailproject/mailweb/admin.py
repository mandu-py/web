from django.contrib import admin
from .models import Log,Maildata,Userinfo

# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['idx','msg']
    list_filter = ['msg']
    
@admin.register(Maildata)
class MailadataAdmin(admin.ModelAdmin):
    list_display = ['idx','indate','title','sender','recipient','datedb','checkdb']
    list_display_links = ['idx','indate','title','sender','recipient','checkdb']
    list_filter = ['recipient','datedb']

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['idx','mailaddress','name']




