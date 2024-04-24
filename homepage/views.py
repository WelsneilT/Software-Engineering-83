from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.views import BooksListView
from books.models import Book
# Create your views here.
@login_required
def home(request):
    # Lấy danh sách sách từ model Book
    slider_books = Book.objects.filter(book_available=True)[:6]

    featured_products = Book.objects.filter(book_available=True)[100:120]
    new_arrivals = Book.objects.filter(book_available=True)[79:99]
    most_view_products= Book.objects.filter(book_available=True)[221:241]
    # Trả về trang chính và truyền danh sách sách vào template
    return render(request, 'index-2.html', {'slider_books': slider_books, 
                                            'featured_products': featured_products, 
                                            'new_arrivals': new_arrivals, 
                                            'most_view_products': most_view_products})