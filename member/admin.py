from django.contrib import admin
from .models import Member, MemberLogin

# Register your models here.
admin.site.register(Member)
admin.site.register(MemberLogin)