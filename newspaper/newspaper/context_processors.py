from django.conf import settings


def blog(request):
    return {'BLOG_URL': settings.BLOG_URL}