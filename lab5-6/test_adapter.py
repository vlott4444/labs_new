from adapter import OldPaymentSystem, PaymentAdapter


def test_adapter():
    old = OldPaymentSystem()
    adapter = PaymentAdapter(old)

    result = adapter.pay("ORDER_100", 150.50)

    assert result["success"] is True
    assert result["amount"] == 150.50

if __name__ == "__main__":
    print("Running adapter tests...")

    try:
        from adapter import OldPaymentSystem, PaymentAdapter

        old = OldPaymentSystem()
        adapter = PaymentAdapter(old)
        result = adapter.pay("ORDER_100", 150.50)

        assert result["success"] == True
        assert result["amount"] == 150.50
        assert "OLD_" in result["transaction"]
        print("✅ Adapter test - PASSED")
    except Exception as e:
        print(f"❌ Adapter test - FAILED: {e}")

    print("\nAdapter tests completed!")