from django.shortcuts import render
from django.http import HttpResponse
import operator
def drinks(requests):
    return HttpResponse('Drinking 3L of water everyday will keep you hydrated')
def foods(requests):
    return HttpResponse('Do not eat junk food, it has high sodium content')

# Create your views here.
