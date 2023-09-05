from legacy import Legacy
from util.date import DateTimeUtil

class CRMUtil:

    current_API = Legacy()
    date_util = DateTimeUtil()

    def _complete_customer_object(self, customer: dict) -> dict:
        product_count = 0
        revenue = 0
        orders = self.current_API.get_orders(customer_id=customer["id"])
        for order in orders:
            products = order["products"]
            for product in products:
                product_count += 1
                revenue += float(product["details"]["price"])

        customer["products_ordered"] = product_count
        customer["revenue"] = revenue

        return customer

    def get_customers(self, sorted_by: str=None) -> list:

        if sorted_by not in ["product_volume", "revenue_volume", None]:
            raise Exception()

        customers = self.current_API.get_customers()

        customers = [self._complete_customer_object(customer=customer) for customer in customers]

        if sorted_by == "product_volume":
            customers = sorted(customers, key=lambda d: d['products_ordered'], reverse=True)
        if sorted_by == "revenue_volume":
            customers = sorted(customers, key=lambda d: d['revenue'], reverse=True) 

        return customers

    def get_customer(self, customer_id: str) -> dict:

        customer = self.current_API.get_customer(customer_id=customer_id)
        customer = self._complete_customer_object(customer=customer)

        customer["toto"] = "titi"
        return customer