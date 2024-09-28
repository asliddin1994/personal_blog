from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'is_approved', 'recommended')
    list_filter = ('is_approved', 'recommended')
    search_fields = ('title', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on', 'is_parent')
    list_filter = ('post', 'created_on')
    search_fields = ('name', 'email', 'msg')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

