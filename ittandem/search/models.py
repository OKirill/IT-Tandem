from django.db import models


class Parent(models.Model):

    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=128, verbose_name='Название тега')

    def __str__(self):
        return self.name


class Tag(models.Model):

    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=128, verbose_name='Название тега')
    desc = models.TextField(verbose_name='Описание тега')
    parents = models.ForeignKey(Parent, related_name='parents', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
