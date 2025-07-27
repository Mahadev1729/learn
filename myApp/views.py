from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        'name':'Mahadev',
        'age':23,
        'nationality':'India'
    }
    return render(request,'index.html',context)

def counter(request):
    text=request.GET['text']
    return render(request,'counter.html')
