from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .models import is_visit_long, get_duration, format_duration


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)
    for visit in visits:
        duration = get_duration(visit)
        how_long_was_in = format_duration(duration)
        suspicious_visit = is_visit_long(visit)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': how_long_was_in,
                'is_strange': suspicious_visit
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
