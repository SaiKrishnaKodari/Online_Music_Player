from django.db import models

# Create your models here.
class song(models.Model):
    name=models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='songs',blank=True)
    def __str__(self):
        return self.name