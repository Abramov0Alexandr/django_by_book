from django.urls import path
from blog.views import DraftPostsListView, index, post_share, post_comment, post_detail, post_search

app_name = 'blog'

urlpatterns = [
    # path('', IndexListView.as_view(), name='post_list'),
    path('', index, name='post_list'),
    path('search/', post_search, name='post_search'),
    path('draft_list/', DraftPostsListView.as_view(), name='draft_list'),
    path('tag/<slug:tag_slug>/', index, name='post_list_by_tag'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
]
