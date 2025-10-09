from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    poster = models.URLField(blank = True, null=True)

    def __str__(self):
        return self.title
    