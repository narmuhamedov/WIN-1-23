from django.db import models

class FilmListModel(models.Model):
    GENRE = (
        ('Комедия', 'Комедия'),
        ('Хоррор', 'Хоррор'),
        ('Драмма', 'Драмма')
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название фильма')
    image = models.ImageField(upload_to='films/', verbose_name='Добавьте фото')
    year = models.DateField(verbose_name='Укажите год выпуска')
    director = models.CharField(max_length=100, verbose_name='Укажите режисера')
    genre = models.CharField(max_length=100, choices=GENRE)
    description = models.TextField(blank=True, verbose_name='Описание фильма')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Afisha(models.Model):
    film = models.CharField(max_length=100, verbose_name='Название фильма Афиша')
    time = models.TimeField(verbose_name='Начало фильма')
    area = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.film


class Slider(models.Model):
    slide = models.URLField()

    def __str__(self):
        return self.slide