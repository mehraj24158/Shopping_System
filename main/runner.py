from shopping import TransactionDB
test = TransactionDB()
test.load("purchase.json")
print(test.get_data_by_name("BoB Stewart"))
print(test.get_data_by_name("MehRAJ AHMED"))
print(test.get_data_by_name("Paul Macneil"))

print(test.get_data_by_customer_id(10))
print(test.get_data_by_customer_id(20))
print(test.get_data_by_customer_id(30))
print()

print(test.get_data_by_purchase_id(2132))