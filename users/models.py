from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=None, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователя'

    def __str__(self):
        return self.username

