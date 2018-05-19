import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


def get_default_random_number():
    return random.randint(1, 100)


class User(AbstractUser):
    birthday = models.DateField()
    random_number = models.IntegerField(default=get_default_random_number)

    class Meta:
        ordering = ('date_joined',)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', args=(self.pk,))
