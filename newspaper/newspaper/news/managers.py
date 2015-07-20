from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet


class BaseNewsQuerySet(QuerySet):

    def published(self):
        return self.filter(publish_date__lte=datetime.now()).order_by('publish_date')


class BaseNewsManager(models.Manager):

    def get_query_set(self):
        return BaseNewsQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()
