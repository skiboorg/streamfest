# Generated by Django 3.1 on 2020-11-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0015_auto_20200115_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='uniqUrl',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Хеш для ссылки (/star/stats/)'),
        ),
    ]
