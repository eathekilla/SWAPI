# Generated by Django 2.2.5 on 2021-07-26 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210726_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.RemoveField(
            model_name='film',
            name='producer',
        ),
    ]
