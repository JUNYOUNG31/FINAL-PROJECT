from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    poster_path = models.CharField(max_length=200)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
