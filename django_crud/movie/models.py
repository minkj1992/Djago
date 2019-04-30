from django.db import models
from django.urls import reverse
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    score = models.FloatField()
    genre = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    length = models.IntegerField()
    director = models.CharField(max_length=4000)
    cast = models.CharField(max_length=4000)
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_edit', kwargs={'pk': self.pk})