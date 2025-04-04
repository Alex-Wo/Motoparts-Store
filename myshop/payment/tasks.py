from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@shared_task
def payment_completed(order_id):
    """
    Задание по отправке уведомления на e-mail при успешной оплате
    """
    order = Order.objects.get(id=order_id)
    # Создать счёт
    subject = f'My Shop - Invoice no. {order_id}'
    message = 'Please, find attached the invoice for your recent purchase'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    # Сгенерировать PDF-файл
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # Прикрепить PDF-файл
    email.attach(f'order_{order_id}.pdf', out.getvalue(), 'application/pdf')
    # Отправить письмо
    email.send()
