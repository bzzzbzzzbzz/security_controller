from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from time_functions import get_duration, format_duration

def storage_information_view(request):
    non_closed_visits = []
    non_leaved_visits = Visit.objects.filter(leaved_at__isnull=True).order_by('entered_at')
    for visit in non_leaved_visits:
        name = visit.passcard.owner_name
        duration = get_duration(visit)
        non_closed_visits.append({
            'who_entered': name,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
