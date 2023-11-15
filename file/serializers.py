from rest_framework import serializers

from .models import File


class FileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('name', 'data')
