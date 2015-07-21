from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.utils import translation


class No404Middleware(object):

    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('news_list'))
        return response


class LocaleMiddleware(object):
    """This middleware checks if we have a language cookie. In that case we use
    that language"""

    def process_request(self, request):
        cookie = settings.LANGUAGE_COOKIE_NAME
        forced_lang = request.GET.get(cookie, None)
        request.forced_lang = forced_lang
        if forced_lang:
            translation.activate(forced_lang)
            request.LANGUAGE_CODE = translation.get_language()
            if hasattr(request, 'session'):
                request.session[translation.LANGUAGE_SESSION_KEY] = forced_lang