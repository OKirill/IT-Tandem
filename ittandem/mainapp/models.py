from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, verbose_name='Аватар')
    about_me = models.TextField(max_length=512, blank=True, verbose_name='О себе')
    status = models.CharField(max_length=10, verbose_name='Статус пользователя', blank=True)


class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    link = models.TextField()


class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    desc = models.TextField(verbose_name='Описание проекта')
    tags = models.ManyToManyField('Tag', related_name='tags')


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название тега')
    desc = models.TextField(verbose_name='Описание тега')


# Свзяи тегов с тегами можно реализовать по разному, но тут нужно будет подумать и потестиовать различные варианты
class RelatedTag(models.Model):
    child_tag = models.ForeignKey(Tag, related_name='children', on_delete=models.CASCADE)
    parent = models.ForeignKey(Tag, related_name='parents', on_delete=models.CASCADE)


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='able', on_delete=models.CASCADE)


class Desire(models.Model):
    user = models.ForeignKey(User, related_name='desires', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='wanting', on_delete=models.CASCADE)
