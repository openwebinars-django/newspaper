from django.conf.urls import patterns, url


urlpatterns = patterns('newspaper.news.views',
    url(r'^$', 'news_list', name='news_list'),
    url(r'^news/add/$', 'news_add', name='news_add'),
    url(r'^news/edit/(?P<newsitem_pk>\d+)/$', 'news_edit', name='news_edit'),
    url(r'^news/delete/(?P<newsitem_pk>\d+)/$', 'news_delete', name='news_delete'),

    url(r'^v2/$', 'news_list_v2', name='news_list_v2'),
    url(r'^v2/news/add/$', 'news_add_v2', name='news_add_v2'),

    url(r'^api/news/$', 'news_list_api', name='news_list_api'),

)
