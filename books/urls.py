from django.urls import path

from books.views import BookListApiView, book_list_view, BookDetailApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
    path('', BookListApiView.as_view(), name='index'),
    path('<int:pk>/', BookDetailApiView.as_view(), name='fun'),
    path('<int:pk>/update/', BookUpdateApiView.as_view(), name='fun'),
    path('<int:pk>/delete/', BookDeleteApiView.as_view(), name='fun'),

    path('v2/', book_list_view, name='fun'),
]