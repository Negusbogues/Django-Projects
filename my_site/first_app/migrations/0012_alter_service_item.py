# Generated by Django 4.0.6 on 2022-11-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_remove_service_description_remove_service_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Item',
            field=models.IntegerField(choices=[(1, 'cake topper'), (2, '2'), (3, '3')], default=1),
        ),
    ]
