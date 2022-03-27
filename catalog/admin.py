from django.contrib import admin
from .models import AuthorModel, AnimeModel, GenreModel

# admin.site.register(AuthorModel)

admin.site.register(StudioModel)
admin.site.register(AnimeModel)
admin.site.register(GenreModel)