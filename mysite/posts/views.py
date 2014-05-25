from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def detail(request, post_id):
    return HttpResponse("You are looking at post %s." % post_id)
    #look at comments in views.py
