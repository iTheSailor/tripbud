from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser as User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .utils import is_ajax

# Create your views here.

###turn likes back on
def first(request):
    post = Post.objects.all()
    # post_likes = Post.objects.total_likes()
    context = {
        'post': post,
        # 'post_likes': post_likes
    }
    return render(request, 'dashboard/first.html', context)

def get_feed(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'dashboard/feed.html', context)

def new_post(request):
    if request.method == 'GET':
        print("GET")
        print(request.GET)
        temp_title= request.GET.get('q')
        respond = HttpResponse(render(request, 'dashboard/newpost.html', {'title': temp_title}))
        return respond

def get_modal(request):
    if request.method == 'GET':
        print("GET")
        print(request.GET)
        respond = HttpResponse(render(request, 'dashboard/modal.html'))
        return respond