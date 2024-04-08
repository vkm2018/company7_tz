from django.contrib import admin

from apps.market.models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
