from django.shortcuts import render

def ball(request):
    return render(request, "games/ballgame/ball.html")

