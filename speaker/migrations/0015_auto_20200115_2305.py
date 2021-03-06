# Generated by Django 2.2.6 on 2020-01-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0014_auto_20200115_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='imageQR',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='QR код'),
        ),
        migrations.AlterField(
            model_name='order',
            name='codeQR',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Случайное число для QR кода'),
        ),
    ]
