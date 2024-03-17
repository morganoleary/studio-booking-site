from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)

# Define an inline admin descriptor for User model
# source: https://docs.djangoproject.com/en/dev/topics/auth/customizing/
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fields = ('first_name', 'last_name', 'email')
    can_delete = False
    verbose_name_plural = 'User Profile Details'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)