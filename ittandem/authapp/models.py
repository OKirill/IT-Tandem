from django.db import models
from django.contrib.auth.models import AbstractUser
# from mainapp.models import Article


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, verbose_name='Аватар')
    about_me = models.TextField(max_length=512, blank=True, verbose_name='О себе')
    status = models.CharField(max_length=10, verbose_name='Статус пользователя', blank=True)
    link = models.TextField(max_length=46, verbose_name='Ссылка на соцсеть', blank=True)
    # user_article = models.ForeignKey(Article, null=True, verbose_name='Статья', on_delete=models.PROTECT)


class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    link = models.TextField()


class Deal(models.Model):

    user = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE, verbose_name='Юзер')
    partner = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE, verbose_name='Партнер')
    status = models.BooleanField(default=False)