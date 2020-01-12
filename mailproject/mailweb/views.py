from django.shortcuts import render
from django.db.models import Count,Case,When
from django.db.models.functions import Substr,TruncMonth,RowNumber
from django.http import HttpResponse
from .forms import RemoteForm,RemoteLocalForm,RemoteUserForm
from .models import Log,Maildata,Userinfo,Remote,RemoteUser,RemoteLocal
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
        mail_count=Count('recipient__mailaddress'),o_count = Count(Case(When(openmail__gt = 1,then=1))),
        p_count = Count(Case(When(openmail__gt = 2,then=1)))
        ).order_by('-mail_count')[:10]
    
    monthdata = data.values(
        'datedb'
        ).annotate(d_month=TruncMonth('datedb'),c_month=Count('d_month'),o_count = Count(Case(When(openmail__gt = 1,then=1))),
        p_count = Count(Case(When(openmail__gt = 2,then=1)))
        ).values('c_month','d_month','o_count','p_count'
        ).order_by('d_month')

    
    opendata = data.values(
        'recipient__name'
        ).annotate(o_count = Count(Case(When(openmail__gt = 1,then=1))),
        p_count = Count(Case(When(openmail__gt = 2,then=1)))       
    ).order_by('-o_count')[:10]

    titledata = data.filter(openmail__gt = 1).values(
        'title',
    ).annotate(
        o_count = Count('openmail')
    ).order_by('-o_count')[:5]
    '''  '''
    titlecount = data.values(
        'title'
    ).annotate(t_count = Count('title'),p_count = Count(Case(When(openmail__gt = 1,then=1)))).order_by('-t_count')[:5]

    


    
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

def remote(request):
    now = datetime.now()
    Maindata = Remote.objects.filter(start_time__year=now.year)
    data = Maindata.values('remote_ip__user_system').annotate(c_system = Count('remote_ip__user_system')).order_by('-c_system')[:10]

    
    monthdata = Maindata.values('remote_ip__user_system').annotate(
        d_month=TruncMonth('start_time'),c_count = Count('d_month')
    ).values('remote_ip__user_system','c_count','d_month')

    datetext = {
        'year' : now.year,
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(1,13),
    }
    context = {'data':data,'datetext':datetext}
    print(monthdata)
    return render(request,'remote.html',context)

def remote_detail(request):
    now = datetime.now()
    return re_detail_month(request,now.year,now.month)

def re_detail_month(request,year,month):
    data = Remote.objects.select_related().filter(start_time__year = year,start_time__month = month).order_by('-start_time')
    now = datetime.now()
    datetext = {
        'year' : year,
        'month' : month,
        'loop_year' : range(now.year,now.year-6,-1),
        'loop_month' : range(1,13),
    }
    
    context = {'Remotedata':data,'datetext':datetext}
    return render(request,'remote_detail.html',context)

def edit_remote(request,idx):
    data = Remote.objects.filter(idx = idx)[0]
    
    if request.method == "POST":
        form = RemoteForm(request.POST)
        
        if form.is_valid():           
            post = form.save(commit=False)
            post.idx = data.idx
            post.start_time = data.start_time
            post.end_time = data.end_time
            post.local_ip = data.local_ip
            post.remote_ip = data.remote_ip
            post.system_text = request.POST["system_text"]
            post.save()
        return HttpResponse("ok")
    else:     
        context = {'data':data}
        return render(request,'edit.html',context)
   

def edit_remotelocal(request,idx):
    data = RemoteLocal.objects.filter(idx = idx)[0]

    if request.method == "POST":
        form = RemoteLocalForm(request.POST)
        print(form)
       
        if form.is_valid():           
            post = form.save(commit=False)
            post.idx = data.idx
            post.user_ip = data.user_ip
            post.user_name = request.POST["user_name"]
            post.save()
        return HttpResponse("ok")
    else:     
        context = {'data':data}
        return render(request,'edit_remotelocal.html',context)


def edit_remoteuser(request,idx):
    data = RemoteUser.objects.filter(idx = idx)[0]
    
    if request.method == "POST":
        form = RemoteUserForm(request.POST)
        print(form)
        print(form.is_valid())
        
        if form.is_valid():           
            post = form.save(commit=False)
            post.idx = data.idx
            post.user_ip = data.user_ip
            post.user_name = request.POST["user_name"]
            post.user_system = request.POST["user_system"]
            print(request.POST["user_name"])
            post.save()
        return HttpResponse("ok")
    else:     
        
        context = {'data':data}
        return render(request,'edit_remoteuser.html',context)
    