from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название тега')
    desc = models.TextField(verbose_name='Описание тега')


# Свзяи тегов с тегами можно реализовать по разному, но тут нужно будет подумать и потестиовать различные варианты
class RelatedTag(models.Model):
    child_tag = models.ForeignKey(Tag, related_name='children', on_delete=models.CASCADE)
    parent = models.ForeignKey(Tag, related_name='parents', on_delete=models.CASCADE)


from authapp.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='able', on_delete=models.CASCADE)


class Desire(models.Model):
    user = models.ForeignKey(User, related_name='desires', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='wanting', on_delete=models.CASCADE)
