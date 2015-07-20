from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class No404Middleware(object):

    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('news_list'))
        return response
