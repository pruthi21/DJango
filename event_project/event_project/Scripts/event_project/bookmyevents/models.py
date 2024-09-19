from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_tickets = models.IntegerField()

    def __str__(self):
        return self.title

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket for {self.event.title} by {self.user.username}'
    
