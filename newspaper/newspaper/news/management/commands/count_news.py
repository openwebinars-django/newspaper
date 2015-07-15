from django.core.management.base import BaseCommand

from newspaper.news.models import News


class Command(BaseCommand):
    help = 'Count news.'

    def handle(self, *args, **options):
        print(News.objects.count())