# Generated by Django 5.0.2 on 2024-03-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_is_in_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='num_in_cart',
            field=models.IntegerField(default=0),
        ),
    ]