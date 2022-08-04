from django.shortcuts import render
from django.http import HttpResponse


def primeira_view(request):
    return HttpResponse('Olá Mundo')