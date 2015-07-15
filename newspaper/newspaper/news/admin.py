from django.contrib import admin

from newspaper.news.models import News


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)