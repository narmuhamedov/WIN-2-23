from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class RunString(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your title')
    description = models.TextField(verbose_name='Enter your description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бегущую строку'
        verbose_name_plural = 'Бегущие строки'


class FilmPostModel(models.Model):
    GENRE = (
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy')
    )
    title = models.CharField(max_length=100, verbose_name="Enter your film name")
    description = models.TextField()
    image = models.ImageField(upload_to='films/')
    cost = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Afisha(models.Model):
    title_film = models.CharField(max_length=100)
    time_title = models.TimeField()
    hall = models.CharField(max_length=10)

    def __str__(self):
        return self.title_film


class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo


class ReviewModel(models.Model):
    choice_film = models.ForeignKey(FilmPostModel, on_delete=models.CASCADE,
                                    related_name='comment_object')
    mark = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1),
                                                              MaxValueValidator(5)])
    text_review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_film} - {self.mark}'
