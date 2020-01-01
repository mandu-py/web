from django.shortcuts import render
from django.db.models import Count,F
from django.db.models.functions import Substr,TruncMonth,RowNumber
from django.http import HttpResponse
from .models import Log,Maildata,Userinfo
from datetime import datetime

# Create your views here.

def index(request):
    data_month = datetime.now().year
    data_month1 = datetime.strptime(str(data_month-1),'%Y').year
    

    data = Maildata.objects.values(
        'datedb','recipient__mailaddress','recipient__name'
        ).filter(datedb__contains=('%s' % data_month1))

    yeardata = data.values(
        'recipient__mailaddress','recipient__name'
        ).annotate(
        mail_count=Count('recipient__mailaddress')
        ).order_by('-mail_count')[:10]
    
    monthdata = data.values(
        'datedb'
        ).annotate(d_month=TruncMonth('datedb'),c_month=Count('d_month')
        ).values('c_month','d_month'
        ).order_by('d_month')
    
    '''  '''
    context = {'data':yeardata,'monthdata':monthdata}
    return render(request,'main.html',context)
def detail(request):
    now = datetime.now()
    return detail_month(request,now.year,now.month)

    '''
    now = datetime.now()
    data = Maildata.objects.select_related().filter(datedb__contains=('%s-%s' % (now.year,now.month)))
    
    context = {'Maildata':data}    
    return render(request,'detail.html',context)
    '''
def detail_year(request,year):
    now = datetime.now()
    data = Maildata.objects.select_related().filter(datedb__contains=('%s' % (year)))
    datetext = {
        'year' : year,
        'month' : '',
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(1,13),
    }
    context = {'Maildata':data,'datetext':datetext} 
    return render(request,'detail.html',context)


def detail_month(request,year,month):
    now = datetime.now()
    searchdate = datetime.strptime(str(year) + '-' + str(month), '%Y-%m')
    if len(str(month)) == 1:
        month = '0' + str(month)
    

    data = Maildata.objects.select_related().filter(datedb__contains=('%s-%s' % (year,month)))
    datetext = {
        'year' : year,
        'month' : month,
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(1,13),
    }
    context = {'Maildata':data} 
    return render(request,'detail.html',{'Maildata':data,'datetext' : datetext})
   