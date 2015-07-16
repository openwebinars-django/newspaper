from django.conf.urls import patterns, url


urlpatterns = patterns('newspaper.news.views',
    url(r'^$', 'news_list', name='news_list'),
    url(r'^news/add/$', 'news_add', name='news_add'),
    url(r'^news/edit/(?P<newsitem_pk>\d+)/$', 'news_edit', name='news_edit'),
)
