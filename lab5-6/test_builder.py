from builder import OrderBuilder


def test_builder():
    order = (OrderBuilder("ORDER_001")
             .set_customer("John")
             .add_item("Laptop", 1000)
             .build())

    assert order["order_id"] == "ORDER_001"
    assert order["customer"] == "John"
    assert order["total"] == 1000


def test_builder_validation():
    builder = OrderBuilder("ORDER_002")

    try:
        builder.build()
        assert False, "Should raise error"
    except ValueError:
        pass

if __name__ == "__main__":
    print("Running builder tests...")

    # Тест 1
    try:
        from builder import OrderBuilder

        order = OrderBuilder("ORDER_001").set_customer("John").add_item("Laptop", 1000).build()
        assert order["order_id"] == "ORDER_001"
        assert order["customer"] == "John"
        assert order["total"] == 1000
        print("✅ Test 1: Basic order - PASSED")
    except Exception as e:
        print(f"❌ Test 1: Basic order - FAILED: {e}")

    # Тест 2
    try:
        from builder import OrderBuilder

        builder = OrderBuilder("ORDER_002")
        builder.build()
        print("❌ Test 2: Validation - FAILED (should raise error)")
    except ValueError:
        print("✅ Test 2: Validation - PASSED")

    print("\nBuilder tests completed!")


if __name__ == "__main__":
    print("Running observer tests...")

    try:
        from observer import Order, EmailNotifier

        order = Order("ORDER_200")
        notifier = EmailNotifier()
        order.attach(notifier)
        order.set_status("paid")
        print("✅ Observer test - PASSED (no errors)")
    except Exception as e:
        print(f"❌ Observer test - FAILED: {e}")

    print("\nObserver tests completed!")
