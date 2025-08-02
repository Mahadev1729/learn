from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true=True
    # feature1.details = 'Our service is very quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Secure'
    # feature2.is_true=True
    # feature2.details = 'We keep your data safe and private'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Reliable'
    # feature3.is_true=False
    # feature3.details = 'Our service is always available and trustworthy'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'User-Friendly'
    # feature4.is_true=True
    # feature4.details = 'Our interface is simple and easy to use'
    
    # features=[feature1,feature2,feature3,feature4]
    features=Feature.objects.all()
    return render(request,'index.html',{'features':features})

def counter(request):
    text=request.POST['text']
    amout_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amout_of_words})
