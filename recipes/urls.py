from django.urls import path

from .views import (
    recipe_detail_list,
    recipe_view,
    recipe_create,
    recipe_update
)

app_name='recipes'
urlpatterns=[
    path("recipes/",recipe_detail_list,name='list'),
    path("create/",recipe_create,name='create'),
    path("<int:id>/edit/",recipe_update,name='update'),
    path('<int:id>',recipe_view,name='detail')
]