from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=250)

    def __str__(self):
       return self.title + ' - ' + self.artist

class Song(models.Model):
    album=models.ForeignKey(Album, on_delete= models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=100)
    is_fav=models.BooleanField(default=False)

    def __str__(self):
       return self.song_title