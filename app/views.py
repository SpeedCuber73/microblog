from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from app.models import Post
from .forms import PostForm


class PostView(View):
    """User's messages"""

    def get(self, request):
        posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            id_parent = request.POST.get("id_parent", None)
            if id_parent is not None:
                form.twit = Post.objects.get(id=id_parent)
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")
