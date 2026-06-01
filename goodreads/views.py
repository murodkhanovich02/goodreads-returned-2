from django.shortcuts import render

from books.models import Review


def landing(request):
    return render(request, 'landing.html')


def home_page(request):
    book_review = Review.objects.all().order_by('-created_at')
    context = {
        'book_review': book_review
    }
    return render(request, 'home.html', context)