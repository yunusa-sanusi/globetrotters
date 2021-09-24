from django import forms
from .models import Category, Post, Tag


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
