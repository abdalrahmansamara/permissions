from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=64)
    time_to_prepare = models.IntegerField()
    serving = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    posted_by = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name