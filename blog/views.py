from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
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


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {
        'form': form,
        'title_bar': 'Create Post',
        'title': 'Create A New Post',
        'btn_text': 'Create Post',
    }

    return render(request, 'blog/create-post.html', context)


def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('single-post', slug=form.data['slug'])

    context = {
        'form': form,
        'title_bar': 'Update Post',
        'title': 'Update Post',
        'btn_text': 'Update Post',
    }

    return render(request, 'blog/create-post.html', context)


def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {
        'post': post
    }

    return render(request, 'blog/delete-post.html', context)
