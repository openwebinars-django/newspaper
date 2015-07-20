from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


from newspaper.news.forms import NewsForm
from newspaper.news.models import News

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from newspaper import settings




'''
def news_list(request):
    news = News.objects.published()
    return render_to_response('news/news_list.html',
                              {'news': news},
                              context_instance=RequestContext(request))
                              
'''    

'''
# Paloma Cortes, Issue: Creacion del listado de noticias paginado

# https://docs.djangoproject.com/en/1.8/topics/pagination/

Importado EmptyPage, PageNotAnInteger y Paginator de django.core.paginator

'''                          
def news_list(request):
    news_filtered = News.objects.filter(
        publish_date__lte=datetime.now()).order_by('publish_date')
    paginator = Paginator(news_filtered, settings.PAGINATION_PAGES) # variable en settings.py

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    return render_to_response('news/news_list.html', {"news": news})
                              



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
