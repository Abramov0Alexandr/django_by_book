from django.urls import path
from blog.views import index, draft_posts_list, post_detail


app_name = 'blog'

urlpatterns = [
    path('', index, name='post_list'),
    path('draft_list/', draft_posts_list, name='draft_list'),
    path('blog/<int:id>/', post_detail, name='post_detail'),
]
