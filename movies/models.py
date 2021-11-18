from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField(null=True)
    genre_ids = models.ManyToManyField(Genre)
    poster_path = models.CharField(max_length=200, null=True)
    vote_count = models.PositiveIntegerField()
    vote_average = models.FloatField()
