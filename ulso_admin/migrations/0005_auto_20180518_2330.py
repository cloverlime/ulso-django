# Generated by Django 2.0.5 on 2018-05-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulso_admin', '0004_auto_20180518_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='committeemember',
            name='phone',
            field=models.CharField(blank=True, default='0XXXX XXXXXX', max_length=15),
        ),
        migrations.AddField(
            model_name='concertoapplicant',
            name='phone',
            field=models.CharField(blank=True, default='0XXXX XXXXXX', max_length=15),
        ),
        migrations.AddField(
            model_name='concertowinner',
            name='phone',
            field=models.CharField(blank=True, default='0XXXX XXXXXX', max_length=15),
        ),
        migrations.AddField(
            model_name='musician',
            name='phone',
            field=models.CharField(blank=True, default='0XXXX XXXXXX', max_length=15),
        ),
    ]
