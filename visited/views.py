from django.shortcuts import render, redirect
from visited.models import Post

def visited(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")

    visited = Post.objects.all()
    context = {"visited": visited}
    return render(request, "visited/visited.html", context)

