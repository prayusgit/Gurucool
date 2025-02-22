from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog-view'),
    path('blog-form/', post_create_view, name='post-create'),
    path('<int:post_id>/', post_detail_view, name='post-detail'),
    path('<int:post_id>/edit/', post_edit_view, name='post-edit'),
    path('<int:post_id>/delete/', post_delete_view, name='post-delete'),
    path('search/', post_search_view, name='post-search')
]
