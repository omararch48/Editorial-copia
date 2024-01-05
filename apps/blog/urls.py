from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    # Paths blog
    path('', views.BlogListView, name='blog'),
    path('<slug:slug>/', views.BlogListCategoryView, name='blog-category'),
    path('post/<slug:slug>/', views.PostView, name='post'),
]