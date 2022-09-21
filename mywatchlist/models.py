from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.CharField(max_length=255)