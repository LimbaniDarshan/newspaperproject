from django.contrib import admin
from django.urls import path

from .views import *
app_name = 'articles'
urlpatterns = [
   
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('api/articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('api/articles/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),

]

