from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, verbose_name='Аватар')
    about_me = models.TextField(max_length=512, blank=True, verbose_name='О себе')
    status = models.CharField(max_length=10, verbose_name='Статус пользователя', blank=True)


class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    link = models.TextField()


from mainapp.models import Tag


class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    desc = models.TextField(verbose_name='Описание проекта')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)


