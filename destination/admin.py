from django.contrib import admin

from .models import Destination, Category, Country


class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Destination, DestinationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
