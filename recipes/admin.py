from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe,RecipeIngredients
# Register your models here.
User=get_user_model()
admin.site.unregister(User)
class UserAdmin(admin.ModelAdmin):
        inlines=[]
        list_display=['username']

admin.site.register(User,UserAdmin)

class RecipeIngredientsInline(admin.StackedInline):
        model=RecipeIngredients
        extra=0
        readonly_fields=['quantity_as_float','as_mks','as_imperial']

class RecipeAdmin(admin.ModelAdmin):
        inlines=[RecipeIngredientsInline]
        list_display=['name','user']
        readonly_fields=['timestamp','updated']
        raw_id_fields=['user'] #give search bar thing

admin.site.register(Recipe,RecipeAdmin)
admin.site.register(RecipeIngredients)