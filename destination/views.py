from django.shortcuts import render, redirect
from destination.forms import DestinationForm
from destination.models import Destination, Category, Country
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
