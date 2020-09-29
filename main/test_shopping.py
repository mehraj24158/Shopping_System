from shopping import TransactionDB
import pytest


@pytest.fixture
def test_load():
    print("\n-----------Setup-------------")
    transactions = TransactionDB()
    transactions.load("purchase.json")
    return transactions


def test_get_data_by_name(test_load):
    data = test_load.get_data_by_name(name)
    assert data == {'name': 'Bob SteWart', 'customer_id': 10, 'purchase_id': [2132, 3532, 7654]}


def test_get_data_by_customer_id(test_load):
    data = test_load.get_data_by_customer_id(10)
    print(data, "Captured Through Printing")
    assert data == {'name': 'Bob Stewart', 'customer_id': 10, 'purchase_id': [2132, 3532, 7654]}


def test_get_data_by_purchase_id(test_load):
    data = test_load.get_data_by_purchase_id(2132)
    assert data == [{'name': 'Bob Stewart', 'customer_id': 10, 'purchase_id': [2132, 3532, 7654]},
                    {'name': 'Paul Macneil', 'customer_id': 30, 'purchase_id': [2132, 6442, 1154]}]



