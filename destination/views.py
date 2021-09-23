from django.shortcuts import render
from .models import Destination, Category, Country
from blog.models import Post


def destinations(request):
    destinations = Destination.objects.all()
    latest_posts = Post.objects.all()[:3]

    context = {
        'destinations': destinations,
        'latest_posts': latest_posts
    }
    return render(request, 'destination/destinations.html', context)


def single_destination(request, slug):
    single_destination = Destination.objects.get(slug=slug)
    latest_posts = Post.objects.all()[:3]
    categories = single_destination.categories.all()

    context = {
        'single_dst': single_destination,
        'latest_posts': latest_posts,
        'categories': categories
    }
    return render(request, 'destination/single-destination.html', context)
