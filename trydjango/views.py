from django.http import HttpResponse
from article.models import Article
import random
from django.template.loader import render_to_string
    
def home_view(request):
    id=random.randint(1,2)
    article=Article.objects.get(id=id)
    article_queryset=Article.objects.all()
    contents={
        "article_queryset":article_queryset,
        "object":article,
        "title":article.title,
        "id":article.id,
        "content":article.content
    }


    HTML_STRING=render_to_string("home-view.html",context=contents)

    return HttpResponse(HTML_STRING)