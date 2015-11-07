from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=='GET':
        return HttpResponse('I am called from a get request')
    elif request.method=='POST':
        return HttpResponse('I am called from a post request')
