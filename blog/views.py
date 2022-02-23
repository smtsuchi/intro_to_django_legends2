from django.shortcuts import redirect, render
from django.http import HttpResponse 

# import all your models to be used
from .models import Post
from django.contrib.auth.models import User

# import all your forms to be used
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm

# import extra functionality (authenticate/loing/logout/messages)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={})

def posts(request):
    my_posts = Post.objects.all()
    print(my_posts)
    return render(request, 'blog/posts.html', context={"posts": my_posts})

def createPost(request):
    form = PostForm()
    if request.method == "POST":
        print('a post was made')
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {
        'form': form
        }
    return render(request, 'blog/createpost.html', context)

def logMeIn(request):
    if request.method == "POST":
        username = request.POST.get('username') #comes from the NAME attribute in html input tag
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f'{user} is logged in!')
            return redirect('index')
    return render(request, 'blog/login.html')

def signUp(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logMeIn')
        else:
            print('form invalid')

    context = {'form': form}
    return render(request, 'blog/signup.html', context)

def logMeOut(request):
    logout(request)
    return redirect('logMeIn')