from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='промокод')
    valid_from = models.DateTimeField(verbose_name='начало скидки')
    valid_to = models.DateTimeField(verbose_name='окончание скидки')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   help_text='Введите значение (0 до 100)', verbose_name='скидка в %')
    active = models.BooleanField(verbose_name='активна')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'купон'
        verbose_name_plural = 'купоны'
