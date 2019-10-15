from django.db import models
from authapp.models import User
from tagapp.models import Stack
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')

    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    desc = models.TextField(verbose_name='Описание проекта')
    tags = models.ManyToManyField(Stack, related_name='tags', blank=True)
