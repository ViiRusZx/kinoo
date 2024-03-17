from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm
from django.views.generic import DetailView


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'main/index.html', data)


def about_as(request):
    return render(request, 'main/about_as.html')


class FilmsDetailView(DetailView):
    model = Films
    template_name = 'main/films_detail.html'
    context_object_name = 'one_film'

def all_films(request):
    films = Films.objects.all()
    return render(request, 'main/all_films.html', {"data": films})


def filtered_films(request):
    filtered_by_years = Films.objects.order_by('-year')
    return render(request, 'main/filtered_by_years.html', {"data": filtered_by_years})


def filtered_films_by_genre(request):
    films_by_genre = Films.objects.order_by('genre')
    return render(request, 'main/films_by_genre.html', {"data": films_by_genre})


def films_by_ratings(request):
    filtered_films_by_ratings = Films.objects.order_by('-rating')
    return render(request, 'main/filtered_films_by_ratings.html', {"data": filtered_films_by_ratings})


def create_films(request):
    error = "Неправильно заполнена форма"
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_films')
        else:
            return error
    form = FilmsForm()
    data = {'form': form, 'error': error}

    return render(request, 'main/create_film.html', data)
