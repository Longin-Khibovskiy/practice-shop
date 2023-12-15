from django.core.mail import send_mail
from .models import OrderItem
from .forms import OrderCreateForm
from cart.views import *
from cart.cart_services import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':  # если форма первый раз отображается то метод будет None, и тогда мы перейдем в else для отображения новой формы
        form = OrderCreateForm(request.POST)
        # отправка данных на сервер
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear_cart()
            send_mail('Заказ Оформлен',
                      'Войдите в админ панель, что бы просмотреть новый заказ.',
                      'l.khibovskiy@gmail.com',
                      ['l.khibovskiy@gmail.com '],
                      fail_silently=True)  # ошибка будет игнорироваться, программа продолжит работу
        return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})


def PaymentForm(request):
    card_number = Cart(request)
    if request.method == 'POST':  # если форма первый раз отображается то метод будет None, и тогда мы перейдем в else для отображения новой формы
        form = PaymentForm(request.POST)
        # отправка данных на сервер
        if form.is_valid():
            card_number = form.save()
            for item in card_number:
                OrderItem.objects.create(
                    card_number=item['card_number'],
                    cardholder_name=item['cardholder_name'],
                    expiration_date=item['expiration_date'],
                    cvv=item['cvv']
                )
            card_number.clear_cart()
            send_mail('Заказ Оформлен',
                      'Войдите в админ панель, что бы просмотреть новый заказ.',
                      'django.project@mail.ru',
                      ['django.project@mail.ru'],
                      fail_silently=True)  # ошибка будет игнорироваться, программа продолжит работу
        return render(request, 'orders/created.html', {'card_number': card_number})
    else:
        form = PaymentForm(request)
    return render(request, 'orders/create.html', {'form_num': form})
