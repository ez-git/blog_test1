from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Article, Comment


def index(request):
    latest_articles_list = Article.objects.order_by('-article_date')[:5]
    return render(request, 'list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Article not found')

