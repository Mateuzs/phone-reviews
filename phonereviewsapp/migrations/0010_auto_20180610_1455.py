# Generated by Django 2.0.5 on 2018-06-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonereviewsapp', '0009_phone_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Price'),
        ),
    ]
