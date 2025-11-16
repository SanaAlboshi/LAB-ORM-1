from django.shortcuts import render
from posts.models import Post

def home_view(request):
    latest_posts = Post.objects.filter(is_published=True)[:6]
    context = {
        'latest_posts': latest_posts,
        'page_title': 'Home'
    }
    return render(request, 'home/home.html', context)