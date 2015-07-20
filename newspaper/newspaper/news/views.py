from datetime import datetime , date, timedelta

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from newspaper.news.forms import NewsForm
from newspaper.news.forms import EventsForm
from newspaper.news.models import News
from newspaper.news.models import Event


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

##################
#vistas de eventos
##################
def events_list(request):
    #fecha desde cuando se puede ver el evento en el listado (FILTRO)
    #muestro solo los futuros y luego los pasados
    #lte -> lees than or equal to fecha actual
    events_future = Event.objects.filter(
        publish_date__lte=datetime.now(),
        start_date__gt=datetime.now()
        ).order_by('start_date')

    events = Event.objects.filter(
        publish_date__lte=datetime.now(),
        start_date__lt=datetime.now(),
        end_date__gt=datetime.now()
        ).order_by('start_date')

    events_past = Event.objects.filter(
        publish_date__lte=datetime.now(),
        end_date__lt=datetime.now()
        ).order_by('end_date')
    #render de la vista
    return render_to_response('events/events_list.html',
                              {
                              'events_future': events_future,   
                              'events': events,
                              'events_past': events_past},
                              context_instance=RequestContext(request))


def events_add(request):
    data = None
    if request.method == 'POST':
        data = request.POST

    #two weeks after    

    date_plus = datetime.now() + timedelta(days=14)    

    initial = {'publish_date': datetime.now(),
               'start_date': datetime.now(),
               'end_date':  date_plus}
    events_form = EventsForm(data=data,
                         initial=initial)
    if events_form.is_valid():
        events_form.save()
        return HttpResponseRedirect(reverse('events_list'))
    return render_to_response('events/events_add.html',
                              {'events_form': events_form},
                              context_instance=RequestContext(request))


def events_edit(request, eventitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    events_item = Event.objects.get(pk=eventitem_pk)
    events_form = EventsForm(data=data,
                         instance=events_item)
    if events_form.is_valid():
        events_form.save()
        return HttpResponseRedirect(reverse('events_list'))
    return render_to_response('events/events_edit.html',
                              {'events_form': events_form},
                              context_instance=RequestContext(request))