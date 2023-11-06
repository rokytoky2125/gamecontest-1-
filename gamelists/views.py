from django.shortcuts import render, redirect

def gamelist(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")
    return render(request, "gamelists/gamelist.html")
