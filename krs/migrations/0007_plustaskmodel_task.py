# Generated by Django 3.1.5 on 2021-06-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krs', '0006_auto_20210607_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='plustaskmodel',
            name='task',
            field=models.CharField(default='<django.db.models.fields.IntegerField> + <django.db.models.fields.IntegerField> = ', max_length=10),
        ),
    ]