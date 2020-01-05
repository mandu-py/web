from django.contrib import admin
from .models import Log,Maildata,Userinfo

# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['idx','msg']
    
    
@admin.register(Maildata)
class MailadataAdmin(admin.ModelAdmin):
    list_display = ['idx','get_date','title','sender','get_recipient','get_name','openmail']
    list_display_links = ['idx','title','sender','get_recipient','get_name']
    search_fields = ('recipient__name','title')
    '''list_filter = ['recipient','datedb']'''
    
    def get_date(self,obj):
        result_date =obj.datedb.strftime('%Y-%m-') + obj.indate
        return result_date
    get_date.admin_order_field = 'datedb'
    get_date.short_description = 'indate'

    def get_readonly_fields(self,request,obj=None):
        if obj:
            return ['idx','recipient','title','sender','datedb','indate','checkdb']
        else:
            return []

    def get_recipient(self,obj):
        return obj.recipient.mailaddress
    get_recipient.admin_order_field = 'recipient'
    get_recipient.short_description = 'recipient'
    def get_name(self,obj):
        return obj.recipient.name
    get_name.admin_order_field = 'recipient'
    get_name.short_description = 'name'
   
@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['idx','mailaddress','name']
    




