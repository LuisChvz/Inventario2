# Generated by Django 2.2.7 on 2020-01-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='sueltas',
            field=models.IntegerField(default=0),
        ),
    ]
