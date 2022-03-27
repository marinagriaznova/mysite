
from django.views.generic import CreateView
from .models import StudioModel, AnimeModel, GenreModel
from .forms import NewAnimeForm, RenewAnimeForm

def index(request):
	num_animes = AnimeModel.objects.all().count()

	return render(
		request,
		'index.html',
		context={
			'num_animes': num_animes
		})

# class BookCreateView(CreateView):
# 	model = BookModel
# 	fields = ('__all__')

def new_anime(request):
	form = NewAnimeForm()
	return render(request, 'catalog/animemodel_form.html', {'form': form}) 
