from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """
    Represents a member/user of the studio.
    """
    member = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.member}"
