# Generated by Django 2.0.5 on 2018-06-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulsosite', '0011_auto_20180605_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
