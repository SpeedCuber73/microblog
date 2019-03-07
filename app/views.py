from django.shortcuts import render
from django.views.generic import View
from app.models import Post


class PostView(View):
    """User's messages"""

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "app/index.html", {"posts": posts})
