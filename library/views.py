from django.shortcuts import render, redirect, get_object_or_404
# forms
from .forms import BookForm
# models
from .models import Book
# others
from django.contrib.auth.decorators import login_required
from .decorators import only_me


# Create your views here.

@login_required
def library_view(request, *args, **kwargs):
    books = Book.objects.all()
    user = request.user
    user_books = user.book_set.all()
    context = {
        'books': books,
        'user_books': user_books,
    }
    return render(request, 'pages/library.html', context)


@login_required
def book_detail_view(request, book_id, *args, **kwargs):
    book = Book.objects.get(id=book_id)
    user = request.user
    user_books = user.book_set.all()
    context = {
        'book': book,
        'user_books': user_books,
        'show_view': True
    }
    return render(request, 'library/book-detail.html', context)


@login_required
def book_create_view(request, *args, **kwargs):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('library:library-view')
    context = {
        'form': form,
    }
    return render(request, 'library/book-form.html', context)


@only_me
@login_required
def book_edit_view(request, book_id, *args, **kwargs):
    book_obj = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book_obj)
    if form.is_valid():
        form.save()
        return redirect('library:library-view')
    context = {
        'form': form,
    }
    return render(request, 'library/book-form.html', context)


@only_me
@login_required
def book_delete_view(request, book_id, *args, **kwargs):
    book_obj = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book_obj.delete()
        return redirect('library:library-view')
    context = {
        'label': 'Delete',
        'book': book_obj
    }
    return render(request, 'library/book-form.html', context)


@login_required
def book_search_view(request, *args, **kwargs):
    search_query = request.GET.get('search_query')
    books = Book.objects.search(search_query)
    context = {
        'books': books,
        'search_query': search_query
    }
    return render(request, 'library/book-search.html', context)


@login_required
def user_books_view(request, *args, **kwargs):
    user = request.user
    user_books = user.book_set.all()
    context = {
        'user_books': user_books,
    }
    return render(request, 'library/user-books.html', context)
