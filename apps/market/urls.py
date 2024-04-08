from django.contrib import admin
from django.urls import path, include

from apps.market.views import IndexView, LikedView

app_name = 'market'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('liked/<int:item_pk>', LikedView.as_view(), name='liked'),
]