from django.conf.urls import patterns, url


urlpatterns = patterns('newspaper.news.views',
    url(r'^$', 'news_list', name='news_list'),
)
