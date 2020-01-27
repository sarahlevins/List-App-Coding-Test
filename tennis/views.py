from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from tennis.models import Player, Nation

class PlayerList(ListView):
    model = Player
    template_name = 'tennis/player_list.html'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'tennis/player_detail.html'