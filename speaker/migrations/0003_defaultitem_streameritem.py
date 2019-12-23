# Generated by Django 2.2.7 on 2019-12-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0002_auto_20191215_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleOneDay', models.CharField(blank=True, max_length=100, null=True, verbose_name='ID билета за 1 день')),
                ('articleTwoDays', models.CharField(blank=True, max_length=100, null=True, verbose_name='ID билета за 2 дня')),
                ('priceOneDay', models.IntegerField(default=0, verbose_name='Цена за 1 день')),
                ('priceTwoDays', models.IntegerField(default=0, verbose_name='Цена за 2 деня')),
            ],
            options={
                'verbose_name': 'Билет по умолчанию',
                'verbose_name_plural': 'Билет по умолчанию',
            },
        ),
        migrations.CreateModel(
            name='StreamerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(blank=True, max_length=100, null=True, verbose_name='Артикул')),
                ('streamer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_item', to='speaker.Speaker', verbose_name='Билет от стримера')),
            ],
            options={
                'verbose_name': 'Стример',
                'verbose_name_plural': 'Стримеры',
            },
        ),
    ]
