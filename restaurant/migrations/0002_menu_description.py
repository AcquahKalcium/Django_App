# Generated by Django 4.1.3 on 2023-08-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
