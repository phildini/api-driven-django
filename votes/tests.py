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