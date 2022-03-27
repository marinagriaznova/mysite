from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-anime', views.new_anime, name="add-anime"),
    ]