from django.contrib import admin

from .models import Category, Comment, Post, Tag, Owner


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Owner)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
