from django.views.generic import *
from django.views.generic.edit import UpdateView, DeleteView # new

from .models import Article
from django.urls import reverse_lazy 


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    
class ArticleDetailView(DetailView): 
    model = Article
    template_name = 'article_detail.html'
class ArticleUpdateView(UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    
class ArticleDeleteView(DeleteView):
    
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    

