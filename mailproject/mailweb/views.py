from django.shortcuts import render
from django.http import HttpResponse
from .models import Log,Maildata,Userinfo

# Create your views here.

def index(request):
    data = Maildata.objects.all()
    context = {'data':data}
    return render(request,'main.html',context)
def detail(request):
    data = Maildata.objects.select_related()
    context = {'Maildata':data}
    print(context)
    return render(request,'detail.html',context)