from legacy import Legacy
from util.date import DateTimeUtil

class CRMUtil:

    current_API = Legacy()
    date_util = DateTimeUtil()

    def get_customers(self) -> list:

        return self.current_API.get_customers()