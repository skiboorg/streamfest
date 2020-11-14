# Generated by Django 3.1 on 2020-11-14 05:06

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticPages', '0010_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticpage',
            options={'verbose_name': 'Текст для статических страниц', 'verbose_name_plural': 'Текст для статических страниц'},
        ),
        migrations.AddField(
            model_name='sponsor',
            name='bg_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18, verbose_name='Цвет бордера'),
        ),
    ]