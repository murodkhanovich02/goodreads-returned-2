from django.urls import path
from .views import BookListView, BookDetailView, AddReview
app_name = 'books'
urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:id>/reviews/', AddReview.as_view(), name='reviews'),
]