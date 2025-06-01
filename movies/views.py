from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Movie, Director, Actor
from .forms import MovieForm, DirectorForm, ActorForm

def index(request):
    movies = Movie.objects.all().order_by('year')
    actors = Actor.objects.all()
    directors = Director.objects.all()
    template = loader.get_template('index.html')
    context = {
        'title': 'Películas',
        'movies': movies,
        'actors': actors,
        'directors': directors
    }
    return HttpResponse(template.render(context, request))

def movies(request):
    movies = Movie.objects.all().order_by('year')
    template = loader.get_template('movies.html')
    context = {
        'title': 'Películas',
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def actors(request):
    actors = Actor.objects.all()
    template = loader.get_template('actors.html')
    context = {
        'title': 'Actores',
        'actors': actors
    }
    return HttpResponse(template.render(context, request))

def directors(request):
    directors = Director.objects.all()
    template = loader.get_template('directors.html')
    context = {
        'title': 'Directores',
        'directors': directors
    }
    return HttpResponse(template.render(context, request))


def movie(request, id):
    movie = Movie.objects.get(id=id)
    template = loader.get_template('movie.html')
    context = {
        'title': movie.title,
        'subtitle': movie.title,
        'banner': movie.banner,
        'movie': movie
    }
    return HttpResponse(template.render(context, request))

def actor(request, id):
    actor = Actor.objects.get(id=id)
    movies = actor.acted_movies.all()
    template = loader.get_template('actor.html')
    context = {
        'title': actor.name,
        'subtitle': actor.name,
        'actor': actor,
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def director(request, id):
    director = Director.objects.get(id=id)
    movies = director.directed_movies.all()
    template = loader.get_template('director.html')
    context = {
        'title': director.name,
        'subtitle': director.name,
        'director': director,
        'movies': movies
    }
    return HttpResponse(template.render(context, request))

def add_movie(request):
    context = {
        'title': 'Añadir película',
        'subtitle': 'Añadir película'
    }
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form, **context})

def add_actor(request):
    context = {
        'title': 'Añadir actor',
        'subtitle': 'Añadir actor'
    }
    if request.method == 'POST':   
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = ActorForm()
    return render(request, 'actor_form.html', {'form': form, **context})

def add_director(request):
    context = {
        'title': 'Añadir director',
        'subtitle': 'Añadir director'
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = DirectorForm()
    return render(request, 'director_form.html', {'form': form, **context})
