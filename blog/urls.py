from django.urls import path
from blog.views import DraftPostsListView, post_detail, IndexListView


app_name = 'blog'

urlpatterns = [
    path('', IndexListView.as_view(), name='post_list'),
    path('draft_list/', DraftPostsListView.as_view(), name='draft_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail'),
]
