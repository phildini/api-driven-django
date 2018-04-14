from django.views.generic import ListView, DetailView

from .models import Vote


class VoteList(ListView):
    model = Vote
    template_name = 'vote_list.html'


class VoteDetail(DetailView):
    model = Vote
    template_name = 'vote.html'
