from django.core import paginator
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from destination.forms import DestinationForm, CommentForm
from destination.models import Destination, Comment
from blog.models import Post


def destinations(request):
    destinations = Destination.objects.all()
    paginator = Paginator(destinations, 4)
    latest_posts = Post.objects.all()[:3]
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'destinations': destinations,
        'latest_posts': latest_posts,
        'page_obj': page_obj,
    }
    return render(request, 'destination/destinations.html', context)


def single_destination(request, slug):
    single_destination = Destination.objects.get(slug=slug)
    latest_posts = Post.objects.all()[:3]
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
        'comments': comments,
        'form': comment_form,
    }
    return render(request, 'destination/single-destination.html', context)


@login_required(login_url='login')
def add_destination(request):
    form = DestinationForm()

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data
            form.save()
            messages.success(request, 'Destination was added successfully')
            return redirect('destinations')

    context = {
        'form': form,
        'title': 'Add Destination',
    }

    return render(request, 'destination/add-destination.html', context)


@login_required(login_url='login')
def update_destination(request, slug):
    destination = Destination.objects.get(slug=slug)
    form = DestinationForm(instance=destination)

    if request.method == 'POST':
        form = DestinationForm(
            request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination was updated successfully')
            return redirect('single-dst', form.data['slug'])

    context = {
        'form': form,
        'title': 'Update Destination',
    }

    return render(request, 'destination/add-destination.html', context)


@login_required(login_url='login')
def remove_destination(request, slug):
    destination = Destination.objects.get(slug=slug)

    if request.method == 'POST':
        destination.delete()
        messages.success(request, 'Destination was removed successfully')
        return redirect('destinations')

    context = {
        'single_dst': destination
    }

    return render(request, 'destination/remove-destination.html', context)
