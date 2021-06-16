from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import  *
from django.core import serializers
# Create your views here.
def homepage(request):
    tracks=track.objects.all()
    music=[obj.__dict__ for obj in tracks]
    # print(music)
    return render(request,'index.html',{'music':music})

def index(request):
    tracks=track.objects.all()
    
    data = serializers.serialize('json', tracks)
    print(data[2:10])
    return HttpResponse(data,content_type="application/json")
    