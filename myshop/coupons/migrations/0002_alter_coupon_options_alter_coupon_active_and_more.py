# Generated by Django 4.2.5 on 2023-10-22 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'купон', 'verbose_name_plural': 'купоны'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(verbose_name='активна'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='промокод'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(help_text='Введите значение (0 до 100)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='скидка в %'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(verbose_name='начало скидки'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(verbose_name='окончание скидки'),
        ),
    ]
