from django.shortcuts import render_to_response


def news_list(request):
    return render_to_response("news/news_list.html")