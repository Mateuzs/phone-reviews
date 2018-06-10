# Generated by Django 2.0.5 on 2018-06-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonereviewsapp', '0005_auto_20180610_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonereview',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], verbose_name='Rating (stars)'),
        ),
    ]