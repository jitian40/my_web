#coding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def index(request):
    string=u"这是一个梗。。。。"
    test=['How','are','you','?']
    list=map(str,range(100))
    return render(request,'index.html',{'test':test,'string':string,'list':list})
def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
