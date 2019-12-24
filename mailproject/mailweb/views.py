from django.shortcuts import render
from django.http import HttpResponse
from .models import Log,Maildata,Userinfo

# Create your views here.

def index(request):
    data = Maildata.objects.all()
    print(data)
    context = {'data':data}
    return render(request,'main.html',context)