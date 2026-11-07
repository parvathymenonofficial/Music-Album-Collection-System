
from django.db import models

class Album(models.Model):

    album_name = models.CharField(max_length=200)

    artist = models.CharField(max_length=200)

    genre = models.CharField(max_length=100)

    year = models.CharField(max_length=10)

    def __str__(self):
        return self.album_name
