# Generated by Django 3.2 on 2022-04-09 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aci_logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aci_name', models.CharField(max_length=2000)),
                ('Datetime', models.DateTimeField(default=datetime.datetime(2022, 4, 9, 12, 4, 26, 975338, tzinfo=utc))),
            ],
        ),
    ]
