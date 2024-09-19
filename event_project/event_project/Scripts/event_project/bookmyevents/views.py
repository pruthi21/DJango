from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket
from .forms import EventForm

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'bookmyevents/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'bookmyevents/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'bookmyevents/event_form.html', {'form': form})

def ticket_book(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        ticket = Ticket(user=request.user, event=event)
        ticket.save()
        return redirect('event_detail', pk=event.id)
    return render(request, 'bookmyevents/ticket_book.html', {'event': event})