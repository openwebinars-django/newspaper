from django.core.urlresolvers import reverse

from rest_framework import serializers

from newspaper.news.models import News


class NewsSerializer(serializers.ModelSerializer):

    href = serializers.SerializerMethodField('get_href_url')

    class Meta:
        model = News
        fields = ('title', 'publish_date', 'href')

    def get_href_url(self, obj):
        url = reverse('news_detail_api', args=(obj.pk,))
        return self.context.get('request').build_absolute_uri(url)


class NewsSerializerComplete(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'description', 'publish_date')