from django import forms
from .models import Event, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'venue', 'ticket_price', 'max_tickets']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = []