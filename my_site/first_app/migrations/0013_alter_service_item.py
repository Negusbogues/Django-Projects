# Generated by Django 4.0.6 on 2022-11-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_alter_service_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Item',
            field=models.CharField(choices=[('CT', 'CAKE TOPPER'), ('GB', 'GOODIE BAG')], max_length=100),
        ),
    ]
