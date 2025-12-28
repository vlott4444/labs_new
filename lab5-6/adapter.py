class OldPaymentSystem:
    def make_payment(self, customer_code: str, amount_in_cents: int) -> dict:
        return {
            "status": "success",
            "transaction_id": f"OLD_{customer_code}_{amount_in_cents}",
            "amount": amount_in_cents / 100
        }


class PaymentAdapter:
    def __init__(self, old_system: OldPaymentSystem):
        self.old_system = old_system

    def pay(self, order_id: str, amount: float) -> dict:
        amount_cents = int(amount * 100)
        customer_code = order_id.replace("ORDER_", "CUST_")

        old_result = self.old_system.make_payment(customer_code, amount_cents)

        return {
            "success": old_result["status"] == "success",
            "transaction": old_result["transaction_id"],
            "amount": old_result["amount"]
        }


