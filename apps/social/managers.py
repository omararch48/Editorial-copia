from django.db import models
from django.db.models import Q


class SocialManager(models.Manager):

    def get_availables_social_networks(self):
        try:
            availables_social_networks = self.filter(active='0')
        except:
            availables_social_networks = []
        return availables_social_networks