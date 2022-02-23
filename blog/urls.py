from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('createpost/', views.createPost, name='createPost'),
    path('login/', views.logMeIn, name='logMeIn'),
    path('logout/', views.logMeOut, name='logMeOut'),
    path('signup/', views.signUp, name='signUp'),
]
