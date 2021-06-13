from django.shortcuts import render
from .models import song
# Create your views here.
def homepage(request):
    songs=song.objects.all()
    music=[obj.__dict__ for obj in songs]
    print(music)
    return render(request,'index.html',{'music':music})