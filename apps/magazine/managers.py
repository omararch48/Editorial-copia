from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q


class MagazineManager(models.Manager):

    def get_availables_magazines(self):
        try:
            available_magazines = self.get_queryset().filter(
                Q(status='0') &
                Q(slug__isnull=False) &
                Q(magazinearticle__isnull=False) &
                Q(magazinearticle__status='0') &
                ~Q(intro_text__isnull=True) &
                ~Q(intro_text='') &
                ~Q(intro_text__regex=r'^\s*$')
            ).distinct()
        except:
            available_magazines = []
        return available_magazines
    
    def get_available_magazine(self, slug):
        try:
            available_magazine = self.get_queryset().get(
                Q(status='0') & Q(slug=slug)
            )
        except:
            available_magazine = None
        return available_magazine
    

class MagazineArticleManager(models.Manager):
    def get_availables_articles(self, magazine):
        try:
            availables_articles = self.get_queryset().filter(
                Q(status='0'), Q(magazine=magazine)
            ).order_by('article_number')
        except:
            availables_articles = []
        return availables_articles
    
    def sides_article(self, magazine, number, side):
        search = True
        article = None
        index = number + side
        while search:
            try: 
                article = self.get_queryset().get(
                    Q(magazine=magazine),
                    Q(article_number=index),
                )
            except ObjectDoesNotExist:
                article = None
            if hasattr(article, 'status'):
                if article.status == '0':
                    search = False
            if index <= 0 or article == None:
                search = False
            index = index + side
        return article