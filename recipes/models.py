from django.db import models
from django.conf import settings
from .validators import validators_for_unit
from .utils import  number_str_to_float
import pint
from django.urls import reverse
# Create your models here.

class Recipe(models.Model):
        user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        name=models.CharField(max_length=220)
        description=models.TextField(blank=True,null=True)
        directions=models.TextField(blank=True,null=True)
        timestamp=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)
        active=models.BooleanField(default=True)

        def get_absolute_path(self):
            return reverse('recipes:detail',kwargs={"id":self.id})
        def get_edit_path(self):
            return reverse('recipes:update',kwargs={"id":self.id})
        def get_ingredients(self):
              return self.recipeingredients_set.all()

class RecipeIngredients(models.Model):
        recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
        name=models.CharField(max_length=220)
        quantity=models.TextField(blank=True,null=True)
        quantity_as_float=models.FloatField(blank=True,null=True)
        unit=models.TextField(blank=True,null=True,validators=[validators_for_unit])
        description=models.TextField(blank=True,null=True)
        directions=models.TextField(blank=True,null=True)
        timestamp=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)
        active=models.BooleanField(default=True)

        def get_absolute_path(self):
            return self.get_absolute_path()
        
        def convert_unit(self,system='mks'):
               ureg=pint.UnitRegistry(system=system)
               if self.quantity_as_float is None:
                      return None
               measure=self.quantity_as_float*ureg[self.unit]
               print(measure)
               return measure
            
        def as_mks(self):
               measurment=self.convert_unit(system='mks')
               return measurment.to_base_units()
        def as_imperial(self):
               measurment=self.convert_unit(system='imperial')
               print(measurment)
               return measurment.to_base_units()

        def save(self,*args,**kwargs):
                qt=self.quantity
                qty , sucess = number_str_to_float(qt)
                if sucess:
                     self.quantity_as_float=qty
                else:
                    self.quantity_as_float=None   
                super().save(self,*args,**kwargs)
