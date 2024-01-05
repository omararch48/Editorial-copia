from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


# Create your views here.
class AuthosListView(ListView):
    template_name = 'authors/authors.html'
    model = Author
    context_object_name = 'authors'

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.get_availables_authors()

# def authors(request):
#     return render(request, 'authors/authors.html')