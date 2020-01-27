from django.shortcuts import render
from django.views.generic import ListView
from tennis.models import Player, Nation

class PlayerList(ListView):
    model = Player
    template_name = 'player_list.html'