from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='userimage/', blank=True)
    age = models.IntegerField()
    introduce = models.CharField(max_length=200)
    email = models.EmailField()
