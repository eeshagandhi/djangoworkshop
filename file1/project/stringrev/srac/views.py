from django.shortcuts import render
import operator
from django.http import HttpResponse
def home(requests):
    return render(requests,'srac/home.html')
def rac(requests):
    mytext=requests.GET['fulltext']
    l=[]
    l1=[]
    s=""
    l=mytext.split()
    for i in l:
        l1.append(i[::-1])
    for i in l1:
        s=s+i
    return render(requests,'srac/rac.html',{'rstring':s})
# Create your views here.
