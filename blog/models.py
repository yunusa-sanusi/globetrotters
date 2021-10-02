from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid


User = get_user_model()


class Owner(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture')
    about = models.TextField()
    facebook_url = models.URLField(null=True)
    twitter_url = models.URLField(null=True)
    instagram_url = models.URLField(null=True)
    linkedin_url = models.URLField(null=True)
    youtube_url = models.URLField(null=True)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    featured_image = models.ImageField(
        upload_to='featured_image')
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    @property
    def imageUrl(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} on {self.post}'


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
