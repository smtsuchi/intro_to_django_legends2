from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={})

def posts(request):
    my_posts = [
        {
            'author': "Coding Summit",
            'title': "Blog Post 1",
            "content": "This is my first post",
            'date_posted': "February 21, 2022"
        },
        {
            'author': "John Smith",
            'title': "Blog Post 2",
            "content": "This is John's first post",
            'date_posted': "February 21, 2022"
        },
        {
            'author': "John Smith",
            'title': "Blog Post 2",
            "content": "This is John's first post",
            'date_posted': "February 21, 2022"
        },
    ]



    return render(request, 'blog/posts.html', context={"posts": my_posts})

def createPost(request):
    return HttpResponse("This is the create post page")