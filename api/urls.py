from django.urls import path
from .views import welcome, movie_list
# movie_list

urlpatterns = [
    path('welcome/', welcome),
    path('movies/', movie_list),
]