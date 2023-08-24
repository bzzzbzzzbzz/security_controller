from django.utils import timezone


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
    if not visit_duration.total_seconds() > minutes * 60:
        return False