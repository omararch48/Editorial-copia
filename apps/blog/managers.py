from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q


class PostsManager(models.Manager):

    def get_availables_posts(self):
        try:
            available_posts = self.filter(
                Q(status='0')
            )
        except:
            available_posts = []
        return available_posts
    
    def get_available_post_by_slug(self, slug):
        try:
            available_post_by_slug = self.get(
                Q(status='0') & Q(slug=slug)
            )
        except:
            available_post_by_slug = []
        return available_post_by_slug

    def get_availables_posts_by_category(self, category_slug):
        try:
            available_posts_by_category = self.filter(
                Q(status='0') & Q(categories__slug=category_slug)
            )
        except:
            available_posts_by_category = []
        return available_posts_by_category
    

# class MagazineArticleManager(models.Manager):
#     def get_availables_articles(self, magazine):
#         try:
#             availables_articles = self.get_queryset().filter(
#                 Q(status='0'), Q(magazine=magazine)
#             ).order_by('article_number')
#         except:
#             availables_articles = []
#         return availables_articles
    
#     def sides_article(self, magazine, number, side):
#         search = True
#         article = None
#         index = number + side
#         while search:
#             try: 
#                 article = self.get_queryset().get(
#                     Q(magazine=magazine),
#                     Q(article_number=index),
#                 )
#             except ObjectDoesNotExist:
#                 article = None
#             if hasattr(article, 'status'):
#                 if article.status == '0':
#                     search = False
#             if index <= 0 or article == None:
#                 search = False
#             index = index + side
#         return article