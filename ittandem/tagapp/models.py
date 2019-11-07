from django.db import models
from authapp.models import User
from django.utils.translation import gettext_lazy as _


class Stack(models.Model):

    class Meta:
        ordering = ('name', )
        verbose_name = _('Навык')
        verbose_name_plural = _('Навыки(заполняет админ)')

    name = models.CharField(max_length=255)
    desc = models.TextField(verbose_name='Описание тега', blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Meta:
        ordering = ('user', )
        verbose_name = _('Умение user')
        verbose_name_plural = _('Умения user')

    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    tag = models.ForeignKey(Stack, related_name='able', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Desire(models.Model):
    user = models.ForeignKey(User, related_name='desires', on_delete=models.CASCADE)
    tag = models.ForeignKey(Stack, related_name='wanting', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username