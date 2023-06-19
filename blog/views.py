from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.published.all()
    return render(request, 'blog/post/index.html', {'posts': posts})


def draft_posts_list(request):
    posts = Post.draft.all()
    return render(request, 'blog/post/draft_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
