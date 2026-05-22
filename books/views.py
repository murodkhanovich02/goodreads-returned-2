from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Books


class BookListView(ListView):
    template_name = 'books/books.html'
    queryset = Books.objects.all()
    context_object_name = 'books'


# class BookListView(View):
#
#     def get(self, request):
#         books = Books.objects.all()
#         context = {
#             'books': books
#         }
#         return render(request, 'books/books.html', context)

class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'id'
    model = Books
    context_object_name = 'book'

# class BookDetailView(View):
#
#     def get(self, request, id):
#         book = Books.objects.get(id=id)
#         context = {
#             'book': book
#         }
#         return render(request, 'books/book_detail.html', context)
