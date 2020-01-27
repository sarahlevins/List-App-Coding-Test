from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from tennis.models import Player, Nation
from tennis.forms import AddPlayerForm

class PlayerList(ListView):
    model = Player
    template_name = 'tennis/player_list.html'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'tennis/player_detail.html'

class PlayerAdd(CreateView):
    model = Player
    form_class = AddPlayerForm
    template_name = 'tennis/player_add.html'
    success_url = reverse_lazy('home')

class PlayerDelete(DeleteView):
    model = Player
    template_name = 'tennis/player_delete.html'
    success_url = reverse_lazy('home')