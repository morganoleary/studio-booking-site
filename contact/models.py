from django.db import models

# Create your models here.
DROPDOWN_CHOICES = [
    ('Mat Pilates for Stabilization', 'Mat Pilates for Stabilization'),
    ('Mat Pilates Flow', 'Mat Pilates Flow'),
    ('Strength and Stretch Movement Class', 'Strength and Stretch Movement Class'),
]

class ContactRequest(models.Model):
    
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    class_interested = models.CharField(max_length=100, choices=DROPDOWN_CHOICES, blank=True, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"You received a message from {self.name} ({self.email})"
