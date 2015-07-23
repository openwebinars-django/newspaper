from rest_framework import serializers

from newspaper.news.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'publish_date')