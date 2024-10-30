from  django.urls import path
# from  news.api.views import article_list_view , article_details_view
from  news.api.views import ArticleListCreateAPIView , ArticleDetailAPIView



urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
]