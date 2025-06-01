from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/", views.movies, name="movies"),
    path("movie/<int:id>/", views.movie, name="movie"),
    path("movie/add/", views.add_movie, name="add_movie"),
    path("director/", views.directors, name="directors"),
    path("director/<int:id>/", views.director, name="director"),
    path("director/add/", views.add_director, name="add_director"),
    path("actor/", views.actors, name="actors"),
    path("actor/<int:id>/", views.actor, name="actor"),
    path("actor/add/", views.add_actor, name="add_actor"),
]