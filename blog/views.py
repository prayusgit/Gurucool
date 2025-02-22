from django.shortcuts import render, redirect, get_object_or_404
# forms
from .forms import *
# models
from .models import *
from django.contrib.auth.models import User
# others
from django.contrib.auth.decorators import login_required
from .decorators import admin_only


# Create your views here.

def blog_view(request, *args, **kwargs):
    posts = Post.objects.all()
    user = request.user
    user_group = user.groups.filter(name='admin')
    is_admin = None
    if user_group.exists():
        is_admin = True
    context = {
        'posts': posts,
        'is_admin': is_admin
    }
    return render(request, 'pages/blog.html', context)


def post_detail_view(request, post_id, *args, **kwargs):
    post = Post.objects.get(id=post_id)
    user = request.user
    user_group = user.groups.filter(name='admin')
    is_admin = None
    if user_group.exists():
        is_admin = True
    context = {
        'post': post,
        'is_admin': is_admin
    }
    return render(request, 'blog/post-detail.html', context)


@admin_only
@login_required
def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('blog:blog-view')
    context = {
        'form': form,
    }
    return render(request, 'blog/post-form.html', context)


@admin_only
@login_required
def post_edit_view(request, post_id, *args, **kwargs):
    post_obj = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post_obj)
    if form.is_valid():
        form.save()
        return redirect('blog:blog-view')
    context = {
        'form': form,
    }
    return render(request, 'blog/post-form.html', context)


@admin_only
@login_required
def post_delete_view(request, post_id, *args, **kwargs):
    post_obj = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_obj.delete()
        return redirect('blog:blog-view')
    context = {
        'delete_page': True,
    }
    return render(request, 'blog/post-form.html', context)


def post_search_view(request, *args, **kwargs):
    search_query = request.GET.get('search_query')
    posts = Post.objects.search(search_query)
    context = {
        'posts': posts,
        'search_query': search_query
    }
    return render(request, 'blog/post-search.html', context)
