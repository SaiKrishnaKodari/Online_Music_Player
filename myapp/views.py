from django.shortcuts import render
from .models import  *
# Create your views here.
def homepage(request):
    tracks=track.objects.all()
    music=[obj.__dict__ for obj in tracks]
    print(music)
    return render(request,'index.html',{'music':music})