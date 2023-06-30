from django import template
from blog.models import Post
from django.db.models import Count


register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_post(count=4):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}


@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]
