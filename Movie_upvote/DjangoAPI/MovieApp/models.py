from django.db import models

# Create your models here.
class Movie(models.Model):
    MovieId = models.AutoField(primary_key = True)
    MovieTitle = models.CharField(max_length=100)
    ReleaseDate = models.DateField()
    Upvotes = models.IntegerField(default=0)