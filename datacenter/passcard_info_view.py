from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    person_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in person_visits:
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": visit.leaved_at - visit.entered_at,
                "is_strange": is_visit_long(visit)
            },
        )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
