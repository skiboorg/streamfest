# Generated by Django 2.2.6 on 2020-02-05 16:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticPages', '0007_callback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, null=True, verbose_name='Вопрос')),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Ответ')),
                ('isActive', models.BooleanField(default=True, verbose_name='Выводить на странице')),
            ],
            options={
                'verbose_name': 'Стать участником Вопрос - Ответ',
                'verbose_name_plural': 'Стать участником Вопросы - Ответы',
            },
        ),
    ]
