# Generated by Django 4.0.6 on 2023-01-01 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0004_passwordgen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordgen',
            name='Special',
        ),
    ]
