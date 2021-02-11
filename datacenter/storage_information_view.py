from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    time_duration = str(duration).split('.')[0]
    return time_duration


def storage_information_view(request):
    non_closed_visits = []
    not_leaved = Visit.objects.filter(leaved_at=None)
    for person in not_leaved:
        duration = Visit.get_duration(person)
        formatted_duration = format_duration(duration)
        non_closed_visits.append(
            {
                "who_entered": person.passcard.owner_name,
                "entered_at": person.entered_at,
                "duration": formatted_duration,
            }
        )
    context = {
            "non_closed_visits": non_closed_visits
        }
    return render(request, 'storage_information.html', context)
