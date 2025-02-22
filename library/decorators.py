from django.contrib.auth.models import User
from .models import Book
from django.http import HttpResponse


def only_me(view_func):
    def wrapper_func(request, book_id, *args, **kwargs):
        user = request.user
        book = Book.objects.get(id=book_id)
        user_books = user.book_set.all()
        if book in user_books:
            return view_func(request, book_id, *args, **kwargs)
        else:
            return HttpResponse('This is not your review.')

    return wrapper_func
