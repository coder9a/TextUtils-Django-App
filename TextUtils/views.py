

from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home')

def capfirst(request):
    return HttpResponse('Capitalize first')

def removepunc(request):
    print(request.GET.get('text'))
    return HttpResponse('Remove Punc')

def newlineremove(request):
    return HttpResponse('New line remove')

def spaceremove(request):
    return HttpResponse('space remove')

def charcount(request):
    return HttpResponse('char count')