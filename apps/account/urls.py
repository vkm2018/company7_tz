from django.urls import path, include

from apps.account.views import LoginView

app_name = 'account'

urlpatterns = [
    path('', LoginView.as_view(), name='login')
]
