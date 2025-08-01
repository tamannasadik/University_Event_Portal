from django.shortcuts import render, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})