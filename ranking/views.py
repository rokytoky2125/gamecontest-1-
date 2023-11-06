from django.shortcuts import render

def rank(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")
    return render(request, "ranking/rank.html")

