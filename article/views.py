from django.shortcuts import render
from .models import Article
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.shortcuts import redirect
from django.db.models import Q

@login_required
def create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        "form":form
    }
    if request.method=="POST":
        if form.is_valid():
            obj=form.save()
            context['form']=ArticleForm()
            return redirect(obj.get_absolute_url())
    return render(request,"articles/create.html",context=context)

def search_view(request):
    query_dict=request.GET
    query=query_dict.get("slug")
    print(query)
    qs=Article.objects.all()
    if query is not None: 
        lookups= Q(title__icontains=query) | Q(content__icontains=query)
        qs=Article.objects.filter(lookups)
    print(qs)
    context={
        "object":qs
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
