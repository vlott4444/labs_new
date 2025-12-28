class OrderBuilder:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.customer = ""
        self.items = []
        self.total = 0.0

    def set_customer(self, customer: str):
        self.customer = customer
        return self

    def add_item(self, name: str, price: float, quantity: int = 1):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        self.total += price * quantity
        return self

    def build(self):
        if not self.customer:
            raise ValueError("Customer is required")
        if not self.items:
            raise ValueError("At least one item is required")
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "items": self.items,
            "total": self.total
        }


