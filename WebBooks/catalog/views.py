from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница сайта Мир Книг")

# Create your views here.
