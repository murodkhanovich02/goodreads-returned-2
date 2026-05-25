from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Books


# class BookListView(ListView):
#     template_name = 'books/books.html'
#     queryset = Books.objects.all()
#     context_object_name = 'books'


class BookListView(View):

    def get(self, request):
        books = Books.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)


        paginator = Paginator(books, 2)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj': page_obj
        }
        return render(request, 'books/books.html', context)

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