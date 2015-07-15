from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    publish_date = models.DateTimeField(_('publish date'))

    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title
