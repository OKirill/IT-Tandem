# Generated by Django 2.2.6 on 2019-11-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='link',
            field=models.TextField(blank=True, max_length=46, verbose_name='Ссылка на соцсеть'),
        ),
    ]
