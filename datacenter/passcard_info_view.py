from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, is_visit_long, format_duration
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visit_filter = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visit_filter:
        visit_duration = get_duration(visit)
        is_strange = is_visit_long(visit)
        this_passcard_visits.append(
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(visit_duration),
            'is_strange': is_strange
        },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
