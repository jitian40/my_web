#coding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import AddForm
def index(request):
    string=u"这是一个梗。。。。"
    test=['How','are','you','?']
    list=map(str,range(100))
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form=AddForm(request.POST)
    return render(request,'index.html',{'test':test,'string':string,'list':list,'form':form})
def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
