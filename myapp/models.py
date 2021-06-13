from django.db import models

# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=40)
    Casting=models.CharField(max_length=20)
    Music_Director=models.CharField(max_length=30)
    def __str__(self):
        return self.title
    
class track(models.Model):
    Album = models.ForeignKey(Album,on_delete =models.CASCADE)
    name=models.CharField(max_length=50)
    Singer=models.CharField(max_length=20)
    audio_file = models.FileField(upload_to='songs',blank=True)
    def __str__(self):
        return self.name
