from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields
from .models import Category, Post, Tag, Comment, Owner


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',
                  'category', 'tags', 'slug')

    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control title', 'placeholder': 'Post Title'}))

    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Post Content'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control list-unstyled'}))

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}))

    slug = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control slug', 'placeholder': 'Slug'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Full Name e.g. Jason Doe'}))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address e.g. Jason@email.com'}))

    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Leave your message'}))
