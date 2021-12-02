from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    username = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
