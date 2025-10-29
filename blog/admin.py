from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="50" style="object-fit:cover; border-radius:5px;" />', obj.image.url)
        return "(No Image)"
    image_preview.short_description = "Preview"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at', 'author')