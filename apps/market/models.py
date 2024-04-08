from django.db import models

from apps.account.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_items', blank=True)

    def __str__(self):
        return f'{self.owner} | {self.name} | {self.price}'

