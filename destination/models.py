from django.db import models
from blog.models import Owner
import uuid


class Destination(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    destination_image = models.ImageField(
        upload_to='images/destination-images/')
    continents = models.ForeignKey(
        'Continent', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city}, {self.country}'

    @property
    def imageUrl(self):
        try:
            img = self.destination_image.url
        except:
            img = ''

        return img


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} on {self.post}'


class Continent(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
