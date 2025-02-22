from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path('', library_view, name='library-view'),
    path('book-form/', book_create_view, name='book-create'),
    path('<int:book_id>/', book_detail_view, name='book-detail'),
    path('<int:book_id>/edit/', book_edit_view, name='book-edit'),
    path('<int:book_id>/delete/', book_delete_view, name='book-delete'),
    path('user-books/', user_books_view, name='user-books'),
    path('search/', book_search_view, name='book-search'),
]
