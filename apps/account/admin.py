from django.contrib import admin

from apps.account.models import User, PhoneNumber

admin.site.register(User)
admin.site.register(PhoneNumber)