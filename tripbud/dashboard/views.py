from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Post, Comment

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all().order_by('-date_posted')
        return render(request, 'dashboard.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text_content = request.POST.get('text_content')
        image = request.FILES.get('image')
        post = Post.objects.create(
            title=title,
            text_content=text_content,
            image=image,
            author=request.user
        )
        return redirect('dashboard:dashboard')  # Redirect to the dashboard or post detail page
    return render(request, 'create_post.html')

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(request, 'post_detail.html', {'post': post})

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        text_content = request.POST.get('text_content')
        image = request.FILES.get('image')
        post.title = title
        post.text_content = text_content
        if image:
            post.image = image
        post.save()
        return redirect('dashboard:dashboard')
    return render(request, 'edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('dashboard:dashboard')

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        text_content = request.POST.get('text_content')
        comment = Comment.objects.create(
            post=post,
            text_content=text_content,
            author=request.user
        )
        return redirect('post_detail', post_id=post.id)  # Redirect to the post detail page
    return render(request, 'add_comment.html', {'post': post})

@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.likes.add(request.user)
        return redirect('dashboard') 
    return redirect('dashboard')  

