# Generated by Django 3.1.5 on 2021-01-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]