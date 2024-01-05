from .models import Link


def social_dict(request):
    links = Link.objects.get_availables_social_networks()
    return {'social_dictionary': links,}