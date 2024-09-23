from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_approved', 'created_on')
    list_filter = ('is_approved', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

