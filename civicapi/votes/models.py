from django.db import models
from django.utils import timezone

class Vote(models.Model):
    subject = models.CharField(max_length=255)
    vote_taken = models.DateTimeField(default=timezone.now)
    ayes = models.IntegerField(blank=True, null=True)
    nays = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{subject} - {ayes}/{nays} on {vote_taken}'.format(
            subject=self.subject,
            ayes=self.ayes,
            nays=self.nays,
            vote_taken=self.vote_taken.strftime('%c'),
        )

