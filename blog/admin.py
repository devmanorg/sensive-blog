from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', )
    list_display = ('title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post')
    list_display = ('post', 'text')
