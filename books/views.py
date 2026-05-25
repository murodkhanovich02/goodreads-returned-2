from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .forms import ReviewForm
from .models import Books, Review


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


class BookDetailView(View):

    def get(self, request, id):
        book = Books.objects.get(id=id)
        review_form = ReviewForm()
        context = {
            'book': book,
            'review_form': review_form
        }
        return render(request, 'books/book_detail.html', context)


class AddReview(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Books.objects.get(id=id)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            Review.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse('books:book_detail', kwargs={'id': book.id}))

        return render(request, 'books/book_detail.html', {'book': book, 'review_form': review_form})
