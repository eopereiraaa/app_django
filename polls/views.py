from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def test(request):
    return HttpResponse("Testando view test")


def test_html(request):
    name = 'criar um index.html dentro de um projeto Django'
    colors = [
        "yellow",
        "red",
        "blue",
        "pink",
    ]
    return render(request=request, template_name='index.html', context={'name': name, 'colors': colors})
