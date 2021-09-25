from django.shortcuts import render, redirect
from destination.forms import DestinationForm, CommentForm
from destination.models import Destination, Comment
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
    comments = Comment.objects.filter(destination=single_destination)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.data['name']
            email = comment_form.data['email']
            content = comment_form.data['content']
            Comment.objects.create(
                name=name, email=email, content=content, destination=single_destination)
            return redirect('single-dst', single_destination.slug)

    context = {
        'single_dst': single_destination,
        'latest_posts': latest_posts,
        'categories': categories,
        'comments': comments,
        'form': comment_form,
    }
    return render(request, 'destination/single-destination.html', context)


def add_destination(request):
    form = DestinationForm()

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return redirect('destinations')

    context = {
        'form': form,
        'title': 'Add Destination',
    }

    return render(request, 'destination/add-destination.html', context)


def update_destination(request, slug):
    destination = Destination.objects.get(slug=slug)
    form = DestinationForm(instance=destination)

    if request.method == 'POST':
        form = DestinationForm(
            request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('single-dst', form.data['slug'])

    context = {
        'form': form,
        'title': 'Update Destination',
    }

    return render(request, 'destination/add-destination.html', context)


def remove_destination(request, slug):
    destination = Destination.objects.get(slug=slug)

    if request.method == 'POST':
        destination.delete()
        return redirect('destinations')

    context = {
        'single_dst': destination
    }

    return render(request, 'destination/remove-destination.html', context)
