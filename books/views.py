from django.shortcuts import render
from django.views import View

from .models import Books


class BookListView(View):

    def get(self, request):
        books = Books.objects.all()
        context = {
            'books': books
        }
        return render(request, 'books/books.html', context)


class BookDetailView(View):

    def get(self, request, id):
        book = Books.objects.get(id=id)
        context = {
            'book': book
        }
        return render(request, 'books/book_detail.html', context)
