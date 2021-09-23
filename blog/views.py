from django.shortcuts import render
from .models import Post
from destination.models import Destination, Category


def index(request):
    destinations = Destination.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    categories = []

    for category in Category.objects.all():
        categories.append(
            {'category': category.name, 'count': Destination.objects.filter(categories=category).count()})

    context = {
        'categories': categories,
        'destinations': destinations,
        'latest_post': latest_post,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def posts(request):
    posts = Post.objects.all()
    latest_posts = Post.objects.all()[:3]

    context = {
        'posts': posts,
        'latest_posts': latest_posts
    }
    return render(request, 'blog/posts.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    latest_posts = Post.objects.all()[:3]
    tags = post.tags.all()
    context = {
        'post': post,
        'tags': tags,
        'latest_posts': latest_posts
    }
    return render(request, 'blog/single-post.html', context)
