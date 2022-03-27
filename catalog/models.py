'''from django.db import models
from django.urls import reverse
import uuid

class AnimeModel(models.Model):
	title = models.CharField(max_length=200) 
	#studio = models.ForeignKey('StudioModel', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=10000, help_text='Краткое содержание книги')
	#genre = models.ManyToManyField('GenreModel', help_text='Выберите жанр')
	def __str__(self):
		return self.title


class GenreModel(models.Model):
	name = models.CharField(max_length=200, help_text='Введите жанр книги')

	def __str__(self):
		return self.name

class StudioModel(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return f'{self.name}'''