from django.shortcuts import render
from .models import Article
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
@login_required
def create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        "form":form
    }
    if request.method=="POST":
        if form.is_valid():
            form.save()
            context['form']=ArticleForm()
    return render(request,"articles/create.html",context=context)

def search_view(request):
    query=request.GET
    query_dict=query.get("q")
    if id is not None:
        article_object=Article.objects.get(id=query_dict)
    context={
        "object":article_object
    }
    return render(request,"articles/search.html",context=context)

def article_view(request,slug):
    article_object=None
    if id is not None:
        article_object=Article.objects.get(slug=slug)
    context={
            "article_object":article_object,
    }
    return render(request, "articles/detail.html", context=context)
