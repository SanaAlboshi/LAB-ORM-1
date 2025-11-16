from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts,
        'page_title': 'All Posts'
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('posts:post_list')
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'page_title': 'Create New Post'
    }
    return render(request, 'posts/post_create.html', context)
