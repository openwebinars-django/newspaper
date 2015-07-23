import json

from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponseRedirect,
                         HttpResponseBadRequest, HttpResponse)
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView, ListView

from rest_framework import generics as rfapiviews
from rest_framework.pagination import PageNumberPagination

from newspaper.news.forms import NewsForm
from newspaper.news.models import News
from newspaper.news.serializers import NewsSerializer


def news_list(request):
    news_filtered = News.objects.published()
    paginator = Paginator(news_filtered, settings.PAGINATION_PAGES)  # variable en settings.py
    page_default = 1

    page = request.GET.get('page', page_default)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(page_default)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    return render_to_response('news/news_list.html',
                              {"news": news},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
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


@login_required(login_url='/admin/')
def news_edit(request, newsitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    news_item = get_object_or_404(News, pk=newsitem_pk)
    news_form = NewsForm(data=data,
                         instance=news_item)
    if news_form.is_valid():
        news_form.save()
        return HttpResponseRedirect(reverse('news_list'))
    return render_to_response('news/news_edit.html',
                              {'news_form': news_form},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def news_delete(request, newsitem_pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    news_item = get_object_or_404(News, pk=newsitem_pk)
    news_item.delete()
    if request.is_ajax():
        return HttpResponse(json.dumps({'status': 'ok'}))
    return HttpResponseRedirect(reverse('news_list'))


class NewsListView(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news'

    def get_queryset(self):
        return self.model.objects.published()


news_list_v2 = NewsListView.as_view()


class NewsAddView(CreateView):
    model = News
    form = NewsForm
    template_name = 'news/news_add.html'
    fields = '__all__'
    success_url = reverse_lazy('news_list_v2')

    def get_context_data(self, *args, **kwargs):
        ctx = super(NewsAddView, self).get_context_data(*args, **kwargs)
        ctx['news_form'] = ctx['form']
        return ctx


news_add_v2 = NewsAddView.as_view()


class NewsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class NewsListAPI(rfapiviews.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

news_list_api = NewsListAPI.as_view()