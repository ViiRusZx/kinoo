from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='home'),
        path('about/', views.about_as, name='about'),
        path('all_films/', views.FilmsListView.as_view(), name='all_films'),
        path('filtered_by_years/', views.FilmsSortedByYearView.as_view(),
             name='filtered_by_years'),
        path('filtered_by_genre/', views.FilmsSortedByGenreView.as_view(), name =
        'filsm_by_genre'),
        path('films_by_ratings/', views.FilmsSortedByRatingsView.as_view(),
             name='films_by_ratings'),
        path('create/', views.create_films, name='create_films'),
        path('films/<int:pk>/', views.FilmsDetailView.as_view(), name='film-detail'),
        ]