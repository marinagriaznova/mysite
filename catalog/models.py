from django.db import models
import uuid

class AnimeModel(models.Model):
	title = models.CharField(max_length=200) 
	studio = models.ForeignKey('StudioModel', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=10000, help_text='Краткое содержание книги')
	country = models.CharField('CountryModel', max_length=13, unique=True)
	genre = models.ManyToManyField('GenreModel', help_text='Выберите жанр')
	numofepisodes = models.TextField(max_length=10)
	year = models.TextField(max_length=10)
	def __str__(self):
		return self.title


class GenreModel(models.Model):
	name = models.CharField(max_length=200, help_text='Введите жанр книги')

	def __str__(self):
		return self.name

class StudioModel(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return f'{self.name}'