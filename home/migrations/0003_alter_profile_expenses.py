# Generated by Django 4.0.3 on 2022-03-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile_expenses_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0),
        ),
    ]
