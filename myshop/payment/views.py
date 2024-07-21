from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from orders.models import Order

# Создаём экземпляр Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

        # Данные сеанса оформления платежа Stripe
        session_data = {'mode': 'payment', 'client_reference_id': order.id, 'success_url': success_url,
                        'cancel_url': cancel_url, 'line_items': []}

        # Добавление позиций товаров в сеанс аформления платёжки
        for item in order.items.all():
            session_data['line_items'].append({'price_data': {'unit_amount': int(item.price * Decimal('100')),
                                                              'currency': 'RUB',
                                                              'product_data': {'name': item.product.name}},
                                               'quantity': item.quantity})

            # Скидка для учёта в Stripe
            if order.coupon:
                stripe_coupon = stripe.Coupon.create(name=order.coupon.code, percent_off=order.discount,
                                                     duration='once')
                session_data['discounts'] = [{'coupon': stripe_coupon.id}]

        # Создание сеанса оформления платежа Stripe
        session = stripe.checkout.Session.create(**session_data)

        # Перенаправление к платёжной форме Stripe
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/process.html', locals())


def payment_completed(request):
    """
    Успешный платёж
    :param request:
    :return: сообщение об успешной оплате
    """
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    """
    Ошибка платежа
    :param request:
    :return: сообщение ошибки платежа
    """
    return render(request, 'payment/canceled.html')
