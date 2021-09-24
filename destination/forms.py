from django import forms
from django import forms
from django import forms
from .models import Destination, Category, Country


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ('title', 'city', 'country', 'content',
                  'destination_image', 'categories', 'slug')

    title = forms.CharField(label='', widget=(forms.TextInput(
        attrs={'class': 'form-control title', 'placeholder': 'Destination Title'})))

    city = forms.CharField(label='', widget=(forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Destination City'})))

    country = forms.ModelChoiceField(queryset=Country.objects.all(), label='Destination Country', widget=forms.Select(
        attrs={'class': 'form-control'}))

    content = forms.CharField(label='', widget=(forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Destination Content'})))

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}))

    slug = forms.SlugField(label='', widget=(forms.TextInput(
        attrs={'class': 'form-control slug', 'placeholder': 'Slug'})))
