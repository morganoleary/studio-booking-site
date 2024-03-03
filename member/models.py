from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    """
    Represents a member/user of the studio.
    """
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MemberLogin(models.Model):
    """
    Stores user login credentials for members.
    """
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"Member: {self.member}, Username: {self.username}"
