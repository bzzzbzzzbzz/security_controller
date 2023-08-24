from django.db import models
from django.utils import timezone

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
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )



def get_duration(visit):
    if not visit.leaved_at:
        time_now = timezone.localtime(timezone.now())
        delta = time_now - visit.entered_at
    else:
        delta = visit.leaved_at - visit.entered_at
    return delta


def format_duration(delta):
    seconds = delta.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{int(hours)}часов:{int(minutes)}минут'

def is_visit_long(visit, minutes=60):
    visit_duration = get_duration(visit)
    if visit_duration.total_seconds() > minutes * 60:
        return True
    return False