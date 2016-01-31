#coding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import AddForm
def index(request):
    return render(request,'index.html')
def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
