# Generated by Django 4.0.6 on 2022-11-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0020_checkout_alter_order_quantity_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='consult',
            name='Phone',
            field=models.IntegerField(),
        ),
    ]
