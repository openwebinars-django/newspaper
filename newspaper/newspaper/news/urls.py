from django.conf.urls import patterns, url


urlpatterns = patterns('newspaper.news.views',

	#noticias
    url(r'^$', 'news_list', name='news_list'),
    url(r'^news/add/$', 'news_add', name='news_add'),
    url(r'^news/edit/(?P<newsitem_pk>\d+)/$', 'news_edit', name='news_edit'),

    #eventos
    url(r'^events/$', 'events_list', name='events_list'),
    url(r'^events/add/$', 'events_add', name='events_add'),
    url(r'^events/edit/(?P<eventitem_pk>\d+)/$', 'events_edit', name='events_edit'),
)
