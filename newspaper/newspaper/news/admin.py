from django.contrib import admin

from newspaper.news.models import News, Event


class NewsAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)