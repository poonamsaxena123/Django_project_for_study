from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello django")


def about(request):
    return HttpResponse("this is next function about")

def detail(request):
    a="this is detail page"
    return HttpResponse(f"the new page --->{a}")