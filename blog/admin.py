from django.contrib import admin

from blog.models import Comment, Post, Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author',]
    list_display =  ['text', 'published_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']
    list_display = ['title', 'slug', 'published_at',]


admin.site.register(Tag)
