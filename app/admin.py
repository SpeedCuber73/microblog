from django.contrib import admin
from app.models import Post


class PostAdmin(admin.ModelAdmin):
    """Messages"""
    list_display = ("id", "user", "text", "twit", "date")

admin.site.register(Post, PostAdmin)
