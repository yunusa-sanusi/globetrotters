from django.conf import settings
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from destination.models import Destination, Continent


api_key = settings.MAILCHIMP_API_KEY
mailchimp_server = settings.MAILCHIMP_SERVER
mailchimp_list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Mailchimp subscription
def mailchimp_subscription(email):
    mailchimp = MailchimpMarketing.Client()
    mailchimp.set_config({
        'api_key': api_key,
        'server': mailchimp_server
    })

    list_id = mailchimp_list_id

    member_info = {
        'email_address': email,
        'status': 'subscribed'
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print(f'response: {response}')
    except ApiClientError as error:
        print(f'An exception occurred: {error.text}')


def index(request):
    destinations = Destination.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    continents = []
    preview = latest_post.content[:300]

    for continent in Continent.objects.all():
        # Getting the destinations for each category
        continents.append({
            'continent': continent.name,
            'count': Destination.objects.filter(continents=continent).count(),
            'slug': continent.slug
        })

    # Handling Newsletter subscription form
    if request.method == 'POST':
        email = request.POST['email']
        mailchimp_subscription(email)
        messages.success(
            request, 'You have successfully subscribed to our newsletter')
        return redirect('blog-home')

    context = {
        'continents': continents,
        'destinations': destinations,
        'latest_post': latest_post,
        'posts': posts,
        'preview': preview
    }

    return render(request, 'blog/index.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request, f'You successfully logged in as {username}')
                return redirect('blog-home')
            else:
                messages.error(
                    request, 'Username or Password Incorrect', extra_tags='danger')

        return render(request, 'blog/login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')


def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    latest_posts = posts[:3]

    context = {
        'posts': page_obj,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/posts.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    latest_posts = Post.objects.all()[:3].order_by('-created_at')
    tags = post.tags.all()
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.data['name']
            email = comment_form.data['email']
            content = comment_form.data['content']
            Comment.objects.create(
                name=name, email=email, content=content, post=post)
            return redirect('single-post', post.slug)

    context = {
        'post': post,
        'tags': tags,
        'latest_posts': latest_posts,
        'comments': comments,
        'form': comment_form,
    }

    return render(request, 'blog/single-post.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post was created successfully')
            return redirect('posts')

    context = {
        'form': form,
        'title_bar': 'Create Post',
        'title': 'Create A New Post',
        'btn_text': 'Create Post',
    }

    return render(request, 'blog/create-post.html', context)


@login_required(login_url='login')
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post was updated successfully')
            return redirect('single-post', slug=form.data['slug'])

    context = {
        'form': form,
        'title_bar': 'Update Post',
        'title': 'Update Post',
        'btn_text': 'Update Post',
    }

    return render(request, 'blog/create-post.html', context)


@login_required(login_url='login')
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post was deleted successfully')
        return redirect('posts')

    context = {
        'post': post
    }

    return render(request, 'blog/delete-post.html', context)
