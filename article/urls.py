from django.urls import path
from article.views import article_view,search_view,create_view

app_name='article'
urlpatterns = [
    path('',search_view,name='search'),
    path('create/',create_view,name='create'),
    path('<slug:slug>/',article_view, name='detail')

]