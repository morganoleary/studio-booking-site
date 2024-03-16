from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# This code was implemented with help from: https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(member=instance)