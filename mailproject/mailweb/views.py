from django.shortcuts import render
from django.db.models import Count,Case,When,IntegerField,F
from django.db.models.functions import Substr,TruncMonth,RowNumber
from django.http import HttpResponse
from .models import Log,Maildata,Userinfo
from datetime import datetime

# Create your views here.
def index(request):
    return index_year(request,datetime.now().year)

def index_year(request,year):  
    now = datetime.now().year
    

    datetext = {
        'year' : year,
        'month' : '',
        'loop_year' : range(now,now-6,-1),
        
    }
      
    data = Maildata.objects.values(
        'datedb','recipient__mailaddress','recipient__name','title'
        ).filter(datedb__year = year)

    yeardata = data.values(
        'recipient__mailaddress','recipient__name'
        ).annotate(
        mail_count=Count('recipient__mailaddress'),o_count = Count(Case(When(openmail__gt = 1,then=1),output_field=IntegerField())),
        p_count = Count(Case(When(openmail__gt = 2,then=1),output_field=IntegerField()))
        ).order_by('-mail_count')[:10]
    
    monthdata = data.values(
        'datedb'
        ).annotate(d_month=TruncMonth('datedb'),c_month=Count('d_month'),o_count = Count(Case(When(openmail__gt = 1,then=1),output_field=IntegerField())),
        p_count = Count(Case(When(openmail__gt = 2,then=1),output_field=IntegerField()))
        ).values('c_month','d_month','o_count','p_count'
        ).order_by('d_month')

    
    opendata = data.values(
        'recipient__name'
        ).annotate(o_count = Count(Case(When(openmail__gt = 1,then=1),output_field=IntegerField())),
        p_count = Count(Case(When(openmail__gt = 2,then=1),output_field=IntegerField()))       
    ).order_by('-o_count')[:10]

    titledata = data.filter(openmail__gt = 1).values(
        'title',
    ).annotate(
        o_count = Count('openmail')
    ).order_by('-o_count')[:5]
    '''  '''
    titlecount = data.values(
        'title'
    ).annotate(t_count = Count('title'),p_count = Count(Case(When(openmail__gt = 1,then=1),output_field=IntegerField()))).order_by('-t_count')[:5]

    


    
    context = {'data':yeardata,'monthdata':monthdata,'opendata':opendata,'titledata':titledata,'titlecount':titlecount,'datetext':datetext}
    return render(request,'main.html',context)
def detail(request):
    now = datetime.now()
    month = getcount(now.year)
    if(len(month) > 0):
        return detail_month(request,now.year,month[len(month)-1]['d_month'].month)
    else:
        return detail_year(request,now.year)
  

def detail_year(request,year):
    now = datetime.now()
    data = Maildata.objects.select_related().filter(datedb__year = year)
    monthcount = getcount(year)
    datetext = {
        'year' : year,
        'month' : '',
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(0,len(monthcount)),
    }
    context = {'Maildata':data,'datetext':datetext} 
    return render(request,'detail.html',context)


def detail_month(request,year,month):
    now = datetime.now()   
    monthcount = getcount(year)
    '''monthcount[int(month)]['d_month']'''

   
    '''data = Maildata.objects.select_related().filter(datedb__contains=('%s-%s' % (year,month)))'''

    data = Maildata.objects.select_related().filter(datedb__year = year,datedb__month = monthcount[int(month)]['d_month'].month)

    
    datetext = {
        'year' : year,
        'month' : month,
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(0,len(monthcount)),
    }
    context = {'Maildata':data,'datetext' : datetext} 
    return render(request,'detail.html',context)




''' # 월별 차수 구하기 '''
def getcount(data_month1):
            month_count = Maildata.objects.values(
        'datedb'
        ).filter(datedb__year=data_month1).annotate(d_month=TruncMonth('datedb'),c_month=Count('d_month')).values('d_month','c_month').order_by('datedb')
        
            return month_count

''' # 월별 차수 데이터 호출 '''



   