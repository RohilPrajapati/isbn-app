from django.urls import path
from books.views import BookSearchAPIView

urlpatterns = [path("", BookSearchAPIView.as_view(), name="book_search_isbn")]
