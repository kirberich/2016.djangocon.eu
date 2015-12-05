from django.db import models
from django.utils import timezone


class Proposal(models.Model):
    class SKILL_LEVEL:
        EVERYONE = 1
        NOVICE = 2
        INTERMEDIATE = 3
        ADVANCED = 4

        choices = [
            (EVERYONE, 'everyone'),
            (NOVICE, 'novice'),
            (INTERMEDIATE, 'intermediate'),
            (ADVANCED, 'advanced'),
        ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    speaker_information = models.TextField(blank=True)
    title = models.TextField()
    description = models.TextField()
    audience = models.TextField()
    props = models.TextField(blank=True)
    skill_level = models.PositiveIntegerField(choices=SKILL_LEVEL.choices, default=SKILL_LEVEL.EVERYONE)
    notes = models.TextField(blank=True)
    mentoring = models.BooleanField(default=False)

    submitted_on = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title