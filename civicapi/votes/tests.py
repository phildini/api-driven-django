from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from .models import Vote
from .serializers import VoteSerializer
from .views import VoteList, VoteDetail

class VoteModelTests(TestCase):

    def test_str(self):
        time = timezone.now()
        vote = Vote.objects.create(
            subject="More projects built in Django",
            ayes=100,
            nays=0,
            vote_taken=time,
        )
        expected_string = "More projects built in Django - 100/0 on {}".format(
            time.strftime('%c'),
        )
        assert expected_string == str(vote)


class VoteSerializerTests(TestCase):

    def test_serialization(self):
        time = timezone.now()
        vote = Vote.objects.create(
            subject="More projects built in Django",
            ayes=100,
            nays=0,
            vote_taken=time,
        )
        serialized = VoteSerializer(vote).data
        assert vote.id == serialized['id']
        assert vote.subject == serialized['subject']
        assert vote.ayes == serialized['ayes']
        assert vote.nays == serialized['nays']


class VoteViewTests(TestCase):

    def test_vote_list(self):
        factory = APIRequestFactory()
        request = factory.post('/votes/', {'subject': 'More Django'})
        response = VoteList.as_view()(request)
        assert 201 == response.status_code
