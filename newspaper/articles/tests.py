from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article


class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser1 = User.objects.create_user(username='test1', password='Royal@16')
        testuser1.save()
        
        test_article = Article.objects.create(author=testuser1, title='Blog Title', body='Blog Content')
        test_article.save()

    def test_article_content(self):
        article = Article.objects.get(id=1)
        author = article.author.username  # Get username of the author
        title = article.title
        body = article.body
        date = article.date.strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string for comparison
        
        self.assertEqual(author, 'test1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Blog Content')
        # Date comparison can be adjusted based on your requirements
        self.assertEqual(date, article.date.strftime('%Y-%m-%d %H:%M:%S'))
