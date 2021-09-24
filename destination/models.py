from django.db import models
import uuid


class Destination(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    destination_image = models.ImageField(
        upload_to='destination')
    categories = models.ManyToManyField('Category', blank=True)
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


class Country(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
