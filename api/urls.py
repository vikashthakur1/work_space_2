from django.urls import path
from .views import welcome, movie_list
from .views import review_list_create
# movie_list

urlpatterns = [
    path('welcome/', welcome),
    path('movies/', movie_list),
    path('movies/<int:movie_id>/reviews/', review_list_create),
]
