from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse


def home(request):

    dict = {}

    plantilla = loader.get_template("home.html")
    doc = plantilla.render(dict)

    return HttpResponse(doc)

def test(request):
    dict = {}
    plantilla = loader.get_template("pater.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)