# Generated by Django 2.2.5 on 2021-07-26 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='api.Planet'),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.CharField(max_length=100)),
                ('modified', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('characters', models.ManyToManyField(blank=True, related_name='films', to='api.People')),
                ('planets', models.ManyToManyField(blank=True, related_name='films', to='api.Planet')),
            ],
        ),
    ]
