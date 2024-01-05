from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):

    def get_availables_authors(self):
        try:
            availables_authors = self.filter(status='0')
        except:
            availables_authors = []
        return availables_authors
