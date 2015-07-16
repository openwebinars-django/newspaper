from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from newspaper.news.forms import NewsForm
from newspaper.news.models import News


def news_list(request):
    news = News.objects.filter(
        publish_date__lte=datetime.now()).order_by('publish_date')
    return render_to_response('news/news_list.html',
                              {'news': news},
                              context_instance=RequestContext(request))


def news_add(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    initial = {'publish_date': datetime.now()}
    news_form = NewsForm(data=data,
                         initial=initial)
    if news_form.is_valid():
        news_form.save()
        return HttpResponseRedirect(reverse('news_list'))
    return render_to_response('news/news_add.html',
                              {'news_form': news_form},
                              context_instance=RequestContext(request))


def news_edit(request, newsitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    news_item = News.objects.get(pk=newsitem_pk)
    news_form = NewsForm(data=data,
                         instance=news_item)
    if news_form.is_valid():
        news_form.save()
        return HttpResponseRedirect(reverse('news_list'))
    return render_to_response('news/news_edit.html',
                              {'news_form': news_form},
                              context_instance=RequestContext(request))