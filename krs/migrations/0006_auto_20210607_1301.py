# Generated by Django 3.1.5 on 2021-06-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krs', '0005_remove_plustaskmodel_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='plustaskmodel',
            name='res',
            field=models.IntegerField(default=8),
        ),
        migrations.AddField(
            model_name='plustaskmodel',
            name='x',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='plustaskmodel',
            name='y',
            field=models.IntegerField(default=5),
        ),
    ]