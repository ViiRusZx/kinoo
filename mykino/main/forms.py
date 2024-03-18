from .models import Films
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, Textarea, \
    DateInput, FileInput


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'genre', 'rating', 'year', 'description', 'photo']
        widgets = {'title': TextInput(attrs={'class': 'form-control'}),
                   'genre': TextInput(attrs={'class': 'form-control'}),
                   'rating': NumberInput(attrs={'class': 'form-control'}),
                   'year': DateInput(attrs={'class': 'form-control'}),
                   'description': Textarea(attrs={'class': 'form-control'}),
                   'photo': FileInput(attrs={'class': 'form-control'})}

        widgets = {'title': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                'genre': TextInput(
                        attrs={'class': 'form-control', 'placeholder': ('Жанр '
                                                                        'фильма')}),
                'rating': NumberInput(attrs={'class': 'form-control',
                                             'placeholder': "Рейтинг фильма"}),
                'year': DateTimeInput(
                        attrs={'class': 'form-control', 'placeholder': "Год съёмок "
                                                                       "фильма"}),
                'description': Textarea(attrs={'class': 'form-control',
                                               'placeholder': "Описание фильма"}),
                'photo': FileInput(attrs={'class': 'form-control'})}
