import json
# Database storing transaction information


class TransactionDB:
    def __init__(self):
        self.data = None

    def load(self, file_path):
        with open(file_path) as json_file:
            self.data = json.load(json_file)

    def get_data_by_name(self, name):
        if self.data is None:
            raise Exception("Transaction data not found")

        for transaction in self.data[0]["transactions"]:
            if transaction["name"].lower() == name.lower():
                return transaction
        raise Exception("Name not found")

    def get_data_by_customer_id(self, customer_id):
        if self.data is None:
            raise Exception("Transaction data not found")

        for transaction in self.data[0]["transactions"]:
            if transaction["customer_id"] == customer_id:
                return transaction
        raise Exception("Customer_ID not found")

    def get_data_by_purchase_id(self, purchase_id):
        if self.data is None:
            raise Exception("Transaction data not found")

        transactions = []

        for transaction in self.data[0]["transactions"]:
            for id in transaction["purchase_id"]:
                if id == purchase_id:
                    transactions.append(transaction)

        if not transactions:
            raise Exception("Purchase_ID not found")
        else:
            return transactions

