from django.urls import path
from . import views


app_name = 'core'


urlpatterns = [
    # Paths core
    path('', views.home, name='home'),
    path('howto/', views.howto, name='howto'),
    path('us/', views.us, name='us'),
]