from django.shortcuts import render, get_object_or_404
from articles.models import Article
# Create your views here.


def index(request):
    return render(request, 'index.html', {'articles': Article.objects.all()})


def get_artcile(request, id):
    data = {
        'article': get_object_or_404(Article, id=id),
    }
    return render(request, 'article/article.html', data)