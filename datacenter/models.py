from django.db import models
from datetime import datetime
from django.utils.timezone import utc


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def get_duration(visit):
    now = datetime.utcnow().replace(tzinfo=utc)
    entered_at = visit.entered_at
    duration = now - entered_at
    return duration


def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        return (visit.leaved_at - visit.entered_at).seconds > (minutes * 60)
    return datetime.now()
