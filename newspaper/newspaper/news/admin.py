from django.contrib import admin

from newspaper.news.models import News, Event


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')
    list_filter = ('publish_date',)
    search_fields = ('title',)


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)