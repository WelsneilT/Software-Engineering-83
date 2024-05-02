from django.urls import path
from .views import BooksListView, BooksDetailView, BookCheckoutView, paymentComplete, SearchResultsListView, ShopBooksListView, AdventureBooksListView , BiographyBooksListView, DramaBooksListView, FantasyBooksListView, FictionBooksListView, HistoryBooksListView , HorrorBooksListView, MagicBooksListView, NonFictionBooksListView, RomanceBooksListView

urlpatterns = [
    path('list/', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('shop-list/', ShopBooksListView.as_view(), name = "shop-list"),
    path('adventure/', AdventureBooksListView.as_view(), name = 'adventure-books'),
    path('biography/', BiographyBooksListView.as_view(), name = 'biography-books'),
    path('drama/', DramaBooksListView.as_view(), name = 'drama-books'),
    path('fantasy/', FantasyBooksListView.as_view(), name = 'fantasy-books'),
    path('fiction/', FictionBooksListView.as_view(), name = 'fiction-books'),
    path('history/', HistoryBooksListView.as_view(), name = 'history-books'),
    path('horror/', HorrorBooksListView.as_view(), name = 'horror-books'),
    path('magic/', MagicBooksListView.as_view(), name = 'magic-books'),
    path('non-fiction/', NonFictionBooksListView.as_view(), name = 'non-fiction-books'),
    path('romance/', RomanceBooksListView.as_view(), name = 'romance-books'),
]