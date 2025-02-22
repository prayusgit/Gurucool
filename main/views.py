from django.shortcuts import render
from blog.models import Post


# Create your views here.

def home_view(request, *args, **kwargs):
    blog_posts = Post.objects.all()[:5]
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'pages/home.html', context)


def about_view(request, *args, **kwargs):
    return render(request, 'pages/about.html')
