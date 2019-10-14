from django.db import models
from authapp.models import User


class Field(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Stack(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(verbose_name='Описание тега', blank=True)
    field = models.ForeignKey('Field', related_name="fields", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    tag = models.ForeignKey(Stack, related_name='able', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Desire(models.Model):
    user = models.ForeignKey(User, related_name='desires', on_delete=models.CASCADE)
    tag = models.ForeignKey(Stack, related_name='wanting', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username