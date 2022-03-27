'''
from django.views.generic import CreateView
from .models import AnimeModel
from .forms import NewAnimeForm

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
def registration(request):
	form = RegistrationForm()
	return render(request, 'catalog/registration_form.html', {'form': form}) 
def contacts(request):
	form = ContactsForm()
	return render(request, 'catalog/contacts_form.html', {'form': form}) 
def new_titles(request):
	form = NewTitlesForm()
	return render(request, 'catalog/newtitles_form.html', {'form': form}) 
def home_page(request):
	form = HomePageForm()
	return render(request, 'catalog/homepage_form.html', {'form': form}) 
def about_us(request):
	form = AboutUsForm()
	return render(request, 'catalog/aboutus_form.html', {'form': form}) '''