from django.urls import path
from . import views


app_name = 'magazine'


urlpatterns = [
    # Paths magazine
    path('', views.MagazineListView.as_view(), name='magazine'),
    path('<slug:slug>/', views.MagazineArticleView, name='magazine-detail'),
    path(
        '<slug:slug>/introduction/',
        views.MagazineArticleIntroView,
        name='magazine-introduction'
    ),
    path(
        '<slug:slug>/<slug:article_slug>/',
        views.MagazineArticleDetailView,
        name='magazine-article'
    ),
]