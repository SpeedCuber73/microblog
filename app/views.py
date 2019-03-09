from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from app.models import Post
from .forms import PostForm


class PostView(View):
    """User's messages"""

    def get(self, request):
        posts = Post.objects.all()
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")
