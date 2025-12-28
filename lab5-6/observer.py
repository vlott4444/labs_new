class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.status = "pending"
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def set_status(self, status: str):
        self.status = status
        for observer in self.observers:
            observer.update(self.order_id, self.status)


class EmailNotifier:
    def update(self, order_id: str, status: str):
        print(f"[EMAIL] Order {order_id} is now {status}")


