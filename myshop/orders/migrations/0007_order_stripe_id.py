# Generated by Django 4.1 on 2023-08-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250, verbose_name='Stripe_ID'),
        ),
    ]
