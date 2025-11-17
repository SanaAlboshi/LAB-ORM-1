from django.shortcuts import render, redirect, redirect, get_object_or_404

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
        form = PostForm(request.POST, request.FILES)
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


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('posts:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_create.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('posts:post_list')
    
    context = {
        'post': post
    }
    return render(request, 'posts/post_delete.html', context)