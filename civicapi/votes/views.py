from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import (
    BrowsableAPIRenderer,
    JSONRenderer,
    TemplateHTMLRenderer,
)

from .models import Vote
from .serializers import VoteSerializer


class VoteAPIMixin(object):
    renderer_classes = [
        JSONRenderer,
        TemplateHTMLRenderer,
    ]
    queryset = Vote.objects.all().order_by('vote_taken')
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_renderers(self):
        renderer_classes = self.renderer_classes
        if self.request.user.is_staff:
            renderer_classes += [BrowsableAPIRenderer]
        return [renderer() for renderer in renderer_classes]


class VoteList(VoteAPIMixin, generics.ListCreateAPIView):
    template_name = "vote_list.html"

    def create(self, request, *args, **kwargs):
        response = super(VoteList, self).create(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html' and response.status_code == 201:
            return redirect('/votes/')
        return response


class VoteDetail(VoteAPIMixin, generics.RetrieveUpdateDestroyAPIView):
    template_name = "vote.html"
