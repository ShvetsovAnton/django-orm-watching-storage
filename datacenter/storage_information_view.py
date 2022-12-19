from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration, get_duration
from django.utils.timezone import localtime


def storage_information_view(request):
    who_inside_storage = Visit.objects.filter(leaved_at=None)
    for visit in who_inside_storage:
        duration = get_duration(visit)
        how_long_in_storage = format_duration(duration)
        enteread_at = localtime(visit.entered_at)
        non_closed_visits = [
            {
                'who_entered': visit.passcard,
                'entered_at': enteread_at,
                'duration': how_long_in_storage,
            }
        ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
