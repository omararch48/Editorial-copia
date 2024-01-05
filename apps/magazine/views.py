from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Magazine, MagazineArticle


class ArticleAux:
    status = ''
    article_number = -1


# Create your views here.
class MagazineListView(ListView):
    model = Magazine
    context_object_name = 'magazines'
    template_name = 'magazine/magazine.html'

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.get_availables_magazines()


def MagazineArticleView(request, slug):
    magazine = Magazine.objects.get_available_magazine(slug=slug)
    try:
        articles = MagazineArticle.objects.get_availables_articles(
            magazine=magazine.id
        )
    except:
        articles = []
    if not magazine or not articles:
        return redirect('magazine:magazine')
    context = {'magazine': magazine, 'articles': articles}
    return render(request, 'magazine/magazine_detail.html', context)


def MagazineArticleIntroView(request, slug):
    magazine = Magazine.objects.get_available_magazine(slug=slug)
    try:
        articles = MagazineArticle.objects.get_availables_articles(
            magazine=magazine.id
        )
    except:
        articles = []
        return redirect('magazine:magazine')
    article = articles[0] if len(articles) > 0 else ArticleAux()
    if article.status != '0' or magazine.status != '0':
        return redirect('magazine:magazine')
    context = {'magazine': magazine, 'article': article}
    return render(request, 'magazine/magazine_introduction.html', context)


def MagazineArticleDetailView(request, slug, article_slug):
    magazine = Magazine.objects.get_available_magazine(slug=slug)
    try:
        article = MagazineArticle.objects.get(slug=article_slug)
    except:
        article = ArticleAux()
    article_left = MagazineArticle.objects.sides_article(
        magazine=magazine.id, number=article.article_number, side=-1
    )
    article_right = MagazineArticle.objects.sides_article(
        magazine=magazine.id, number=article.article_number, side=1
    )
    if article.status != '0' or magazine.status != '0':
        return redirect('magazine:magazine')
    context = {
        'magazine': magazine,
        'article': article,
        'article_left': article_left,
        'article_right': article_right
    }
    return render(request, 'magazine/magazine_article.html', context)
