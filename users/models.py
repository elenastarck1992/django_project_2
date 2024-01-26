from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='аватар', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='страна', null=True, blank=True)
