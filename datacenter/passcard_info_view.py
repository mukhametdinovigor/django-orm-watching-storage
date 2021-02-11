from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from django.shortcuts import render
from datetime import datetime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    person_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in person_visits:
        if not visit.leaved_at:
            duration = datetime.now() - visit.entered_at.replace(tzinfo=None)
        else:
            duration = visit.leaved_at - visit.entered_at
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": duration,
                "is_strange": is_visit_long(visit)
            },
        )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
