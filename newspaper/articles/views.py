from django.views.generic import *
from django.views.generic.edit import UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from django.urls import reverse_lazy 
from .serializers import ArticleSerializer

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)
    login_url = 'login'
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, UserPassesTestMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login' 
    
    def test_func(self): # new
        return self.request.user.is_authenticated
    
class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView): 
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
    
    def test_func(self): 
        return self.request.user.is_authenticated
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login' 
    
    def test_func(self): 
        return self.request.user.is_authenticated
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login' 
    
    def test_func(self): 
        return self.request.user.is_authenticated


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    
class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
