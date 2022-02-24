from django.shortcuts import redirect, render
from django.http import HttpResponse 

# import all your models to be used
from .models import Post
from django.contrib.auth.models import User

# import all your forms to be used
from .forms import PostForm, SignUpForm

# import extra functionality (authenticate/loing/logout/messages)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# import mail dependencies
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={})

def posts(request):
    my_posts = Post.objects.all()
    print(my_posts)
    return render(request, 'blog/posts.html', context={"posts": my_posts})

@login_required(login_url='logMeIn')
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
    if request.user.is_authenticated:
        return redirect('index')
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
    if request.user.is_authenticated:
        return redirect('index')
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account successfully created for {username}")

            # EMAIL AUTOMATION
            email = form.cleaned_data.get('email')

            template = render_to_string('blog/emailtemplate.html', {'username': username})

            email_message = EmailMessage(
                'Welcome to my Django Blog!', # subject line
                template, # body
                settings.EMAIL_HOST_USER, # from
                [email], #list of recipients
            )

            email_message.fail_silently = True
            email_message.send()            


            return redirect('logMeIn')
        else:
            print('form invalid')

    context = {'form': form}
    return render(request, 'blog/signup.html', context)

@login_required
def logMeOut(request):
    logout(request)
    return redirect('logMeIn')

    
def individualPost(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}
    return render(request, 'blog/individualpost.html', context)

@login_required
def deletePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        messages.warning(request, "You cannot delete another user's post.")
        return redirect('posts')
    post.delete()
    messages.success(request, "The post was successfully deleted.")
    return redirect('posts')

@login_required
def updatePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        messages.warning(request, "You cannot update another user's post.")
        return redirect('individualPost', post_id = post_id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('individualPost', post_id = post_id)
    context = {"form": form, "post": post}
    return render(request, 'blog/updatepost.html', context)
