import pytest
from src.fraud_detection import detect_fraud

def test_detect_fraud():
    transaction_data = {"id": "tx_001", "amount": 500}
    result = detect_fraud(transaction_data)
    assert "insight" in result
    assert "fraud_score" in result
    assert 0 <= result["fraud_score"] <= 1
