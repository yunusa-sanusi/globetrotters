from django.contrib import admin

from .models import Destination, Continent, Comment


class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Continent, ContinentAdmin)
