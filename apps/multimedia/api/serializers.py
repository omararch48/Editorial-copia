from rest_framework import serializers
from apps.multimedia.models import MediaImage


class KeyMediaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ['id', 'name', 'get_url',]