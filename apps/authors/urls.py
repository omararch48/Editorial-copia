from django.urls import path
from . import views


app_name = 'authors'


urlpatterns = [
    # Paths core
    path('', views.AuthosListView.as_view(), name='authors'),
]