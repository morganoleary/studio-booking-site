from django.db import models
from django.core.validators import MinValueValidator
from member.models import Member

# Create your models here.
class ClassDetails(models.Model):
    DURATION_CHOICES = [
        ('Mat Pilates for Stabilization', '30 minutes'),
        ('Mat Pilates Flow', '45 minutes'),
        ('Strength and Stretch Movement Class', '60 minutes'),
    ]

    CLASS_CHOICES = [
        ('Mat Pilates for Stabilization', 'Mat Pilates for Stabilization'),
        ('Mat Pilates Flow', 'Mat Pilates Flow'),
        ('Strength and Stretch Movement Class', 'Strength and Stretch Movement Class'),
    ]

    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100, choices=CLASS_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50, choices=DURATION_CHOICES)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.class_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    booked_class = models.ForeignKey(ClassDetails, on_delete=models.CASCADE)
    class_date = models.DateField()
    class_time = models.TimeField()

    def __str__(self):
        return f"{self.member} booked {self.booked_class} on {self.class_date}. This class begins at {self.class_time}."