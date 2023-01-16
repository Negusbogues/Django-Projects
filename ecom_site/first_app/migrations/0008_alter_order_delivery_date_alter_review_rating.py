# Generated by Django 4.0.6 on 2022-11-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_rename_delivery_date_order_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Delivery_Date',
            field=models.DateField(verbose_name=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]