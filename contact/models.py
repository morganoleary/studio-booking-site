from django.db import models

# Create your models here.
class DropdownObject(models.Model):
    DROPDOWN_CHOICES = [
        ('Mat Pilates for Stabilization', 'Mat Pilates for Stabilization'),
        ('Mat Pilates Flow', 'Mat Pilates Flow'),
        ('Strength and Stretch Movement Class', 'Strength and Stretch Movement Class'),
    ]

    name = models.CharField(max_length=100, choices=DROPDOWN_CHOICES)

    def __str__(self):
        return self.name

class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    class_interested = models.ForeignKey(DropdownObject, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"You received a message from {self.name} ({self.email})"
