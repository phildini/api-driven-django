from django.shortcuts import redirect

from rest_framework import generics

from rest_framework.renderers import (
    BrowsableAPIRenderer,
    JSONRenderer,
    TemplateHTMLRenderer,
)

from .models import Vote
from .serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    renderer_classes = (
        JSONRenderer,
        TemplateHTMLRenderer,
        BrowsableAPIRenderer,
    )
    template_name = "vote_list.html"
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        response = super(VoteList, self).create(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html' and response.status_code == 201:
            return redirect('/votes/')
        return response

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = (
        JSONRenderer,
        TemplateHTMLRenderer,
        BrowsableAPIRenderer,
    )
    template_name = "vote.html"
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


