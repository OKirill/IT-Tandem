from django.db import models
from authapp.models import User


class Article(models.Model):
    header = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    content = models.CharField(verbose_name='Текст статьи',max_length=500000)
    author = models.ForeignKey(User,verbose_name='Автор статьи', on_delete=models.PROTECT)
