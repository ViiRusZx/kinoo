from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views import View


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'main/index.html', data)


def about_as(request):
    return render(request, 'main/about_as.html')


class FilmsDetailView(DetailView):
    model = Films
    template_name = 'main/films_detail.html'
    context_object_name = 'one_film'


class FilmsListView(ListView):
    model = Films
    template_name = 'main/all_films.html'
    context_object_name = 'films'


class FilmsSortedByYearView(View):
    def get(self, request):
        films_by_year = Films.objects.order_by('-year')
        return render(request, 'main/filtered_by_years.html', {"data": films_by_year})


# def filtered_films(request):
#     filtered_by_years = Films.objects.order_by('-year')
#     return render(request, 'main/filtered_by_years.html', {"data": filtered_by_years})

class FilmsSortedByGenreView(View):
    def get(self, request):
        films_by_genre = Films.objects.order_by('genre')
        return render(request, 'main/films_by_genre.html', {"data": films_by_genre})


class FilmsSortedByRatingsView(View):
    def get(self, request):
        filtered_films_by_ratings = Films.objects.order_by('-rating')
        return render(request, 'main/filtered_films_by_ratings.html',
                      {"data": filtered_films_by_ratings})


def create_films(request):

    if request.method == 'POST':
        form = FilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_films')
        else:
            return None
    form = FilmsForm()
    data = {'form': form}

    return render(request, 'main/create_film.html', data)
