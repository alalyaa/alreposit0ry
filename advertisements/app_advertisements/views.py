from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Успешно! Это главная страница')

def page1(request):
    return HttpResponse('Успешно! Это обычная страница')


