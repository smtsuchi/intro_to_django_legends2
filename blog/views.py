from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("Hey there! this is our blog home page!")

def posts(request):
    return HttpResponse("This is the posts page")

def createPost(request):
    return HttpResponse("This is the create post page")