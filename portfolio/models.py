from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='userimage/', blank=True)
    age = models.IntegerField()
    introduce = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Guestbook(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.content

class FileUpload(models.Model):
    title = models.TextField(max_length=50)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title