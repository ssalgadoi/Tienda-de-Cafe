# Generated by Django 4.2.5 on 2023-09-14 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 3, 42, 45, 337235, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion'),
        ),
    ]
