# Generated by Django 4.1.3 on 2023-02-23 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_user_orders_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='staus',
            new_name='status',
        ),
    ]