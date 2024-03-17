from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='home'),
        path('about/', views.about_as, name='about'),
        path('all_films/', views.all_films, name='all_films'),
        path('filtered_by_years/', views.filtered_films, name='filtered_by_years'),
        path('filtered_by_genre/', views.filtered_films_by_genre, name =
        'filsm_by_genre'),
        path('films_by_ratings/', views.films_by_ratings, name='films_by_ratings'),
        path('create/', views.create_films, name='create_films'),
        path('films/<int:pk>/', views.FilmsDetailView.as_view(), name='film-detail'),
        ]