from django.contrib import admin
from .models import UserProfile, Guestbook

admin.site.register(UserProfile)
admin.site.register(Guestbook)