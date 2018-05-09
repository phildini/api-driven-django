from django.test import TestCase
from django.utils import timezone

from .models import Vote

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