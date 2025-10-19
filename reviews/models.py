from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=255)   
    imdb_id = models.CharField(max_length=20, blank=True, null=True)  
    rating = models.IntegerField(default=1 , validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.movie_title}"