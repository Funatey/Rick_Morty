from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    username = models.CharField(max_length=255, verbose_name='Псевдоним', unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name