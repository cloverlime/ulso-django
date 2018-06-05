# Generated by Django 2.0.5 on 2018-06-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulsosite', '0004_account_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(blank=True, choices=[('Matched', 'Matched'), ('Equipment', 'Equipment'), ('Facilities', 'Facilities'), ('Self-Raised Funds', 'Self-Raised Funds'), ('Cashbox', 'Cashbox')], max_length=10, null=True),
        ),
    ]
