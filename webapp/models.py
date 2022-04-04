from datetime import datetime
from django.db import models

# Create your models here.
class song(models.Model):
    songname=models.CharField(max_length=400)
    worship_date=models.DateTimeField(blank=True,default=datetime.now)
    updated_date=models.DateTimeField(blank=True,default=datetime.now)

class songdetail(models.Model):
    song_id=models.ForeignKey(song,on_delete=models.CASCADE)
    order=models.IntegerField()
    song_text=models.TextField(default="")

    def __iter__(self):
        return [self.song_id,self.order,self.song_text]
