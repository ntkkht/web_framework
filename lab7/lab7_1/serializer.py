from rest_framework import serializers

from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'published_date',
        )
        model = Video
    model = Video
