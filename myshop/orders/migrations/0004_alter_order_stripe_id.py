# Generated by Django 4.1 on 2023-08-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_stripe_id_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250, verbose_name='Stripe_ID'),
        ),
    ]