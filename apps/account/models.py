from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.number}'

class User(AbstractUser):
    number = models.IntegerField(default=0)
