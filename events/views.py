# views.py
from django.shortcuts import render, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

def home_view(request):
    today = timezone.now()
    events = Event.objects.filter(start_time__gte=today).order_by('start_time')
    year = datetime.now().year
    return render(request, 'events/home.html', {'events': events, 'year': year})

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})
