from django.urls import path
from ebooks.api.views import EbookListCreateAPIView,EbookDetailAPIView,ReviewListCreateAPIView,ReviewDetailCreateAPIView

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name='ebook-detail'),
    path('ebooks/<int:ebook_pk>/review/', ReviewListCreateAPIView.as_view(), name='ebook-detail'),
    path('reviews/<int:pk>/', ReviewDetailCreateAPIView.as_view(), name='review-detail'),
    
    
]