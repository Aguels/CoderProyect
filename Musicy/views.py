from django.shortcuts import render
from django.shortcuts import redirect

def inicio(request):
    return render(request,"Musicy/Inicio.html")

def reinicio(request):
    return redirect('/musicy/')

def about(request):
    return render(request,"Musicy/About.html")