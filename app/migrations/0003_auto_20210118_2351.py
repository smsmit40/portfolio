# Generated by Django 3.1.5 on 2021-01-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210118_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='projid',
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
