from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return HttpResponse('<h1>This is my page</h1>')
def aboutus(requests):
    return HttpResponse('<h1>I am Eesha</h1>')
def hobbies(requests):
    return HttpResponse('<h1>Badminton</h1>')

# Create your views here.
