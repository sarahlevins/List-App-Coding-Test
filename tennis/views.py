from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from tennis.models import Player, Nation, PageViews
from tennis.forms import AddPlayerForm

class PlayerList(ListView):
    model = Player
    template_name = 'tennis/player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_views'] = PageViews.objects.count()
        return context

class PlayerDetail(DetailView):
    model = Player
    template_name = 'tennis/player_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_views'] = PageViews.objects.count()
        return context

class PlayerAdd(CreateView):
    model = Player
    form_class = AddPlayerForm
    template_name = 'tennis/player_add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_views'] = PageViews.objects.count()
        return context

class PlayerDelete(DeleteView):
    model = Player
    template_name = 'tennis/player_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_views'] = PageViews.objects.count()
        return context