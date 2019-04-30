from django.shortcuts import render,redirect
from .parser import parse_movie
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Movie

def home(request):
    return render(request, 'home.html')

def parse(request):
    parse_movie()
    return redirect('movie_list')

class MovieList(ListView):
    model = Movie
    template_name = 'movie_list.html'

class MovieView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'score', 'genre', 'date', 'length', 'director', 'cast', 'image']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'score', 'genre', 'date', 'length', 'director', 'cast', 'image']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDelete(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')