from django.db import models
from authapp.models import User
from tagapp.models import Stack


class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    desc = models.TextField(verbose_name='Описание проекта')
    tags = models.ManyToManyField(Stack, related_name='tags', blank=True)
