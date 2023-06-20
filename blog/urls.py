from django.urls import path
from blog.views import DraftPostsListView, post_detail, IndexListView, post_share, post_comment

app_name = 'blog'

urlpatterns = [
    path('', IndexListView.as_view(), name='post_list'),
    path('draft_list/', DraftPostsListView.as_view(), name='draft_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
]
