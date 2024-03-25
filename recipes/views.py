from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from .models import Recipe,RecipeIngredients
from .forms import RecipeForm,RecipeIngredientForm

# Create your views here.

@login_required
def recipe_detail_list(request):
    qs=Recipe.objects.filter(user=request.user)
    context={
        'object':qs
    }
    return render(request,'recipes/detail-list.html',context=context)

@login_required
def recipe_view(request,id):
    qs=get_object_or_404(Recipe,id=id,user=request.user)
    context={
        'object':qs
    }
    return render(request,'recipes/detail.html',context=context)

@login_required
def recipe_create(request):
    form=RecipeForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user=request.user
        obj.save()
        return redirect(obj.get_absolute_path())
    return render(request,'recipes/create-update.html',context=context)

@login_required
def recipe_update(request,id):
    obj=get_object_or_404(Recipe,id=id,user=request.user)
    form =RecipeForm(request.POST or None, instance=obj)
    RecipeIngredientFormset=modelformset_factory(RecipeIngredients,form=RecipeIngredientForm,extra=0)
    qs=obj.recipeingredients_set.all()
    formset=RecipeIngredientFormset(request.POST or None, queryset=qs)
    context={
        'form':form,
        'formset':formset,
        'object':qs
    }
    if all([form.is_valid() , formset.is_valid()]):
        form.save()
        formset.save()
        context['message']="Reicpe Updated Successfully."
        
    return render(request,'recipes/create-update.html',context=context)
    
