from observer import Order, EmailNotifier


def test_observer():
    order = Order("ORDER_200")
    notifier = EmailNotifier()

    order.attach(notifier)
    order.set_status("paid")
    # Просто проверяем что нет ошибок