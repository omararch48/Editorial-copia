from django.contrib import admin
from .models import Magazine, MagazineArticle


# Register your models here.
admin.site.register(Magazine)
admin.site.register(MagazineArticle)