# Generated by Django 4.1.3 on 2023-01-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='staus',
            field=models.CharField(choices=[('order-placed', 'order-placed'), ('in-cart', 'in-cart'), ('cancelled', 'cancelled')], default='in-cart', max_length=200),
        ),
    ]
