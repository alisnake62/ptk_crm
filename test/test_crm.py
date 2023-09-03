from util.crm import CRMUtil

fake_legacy_product_3 = {
    "createdAt":"2023-08-28T03:16:28.440Z",
    "name":"Rufus Pacocha",
    "details":{
        "price":"97.00",
        "description":"The Football Is Good For Training And Recreational Purposes",
        "color":"red"
    },
    "stock":73254,
    "id":"3"
}
fake_legacy_product_53 = {
    "createdAt":"2023-08-29T22:55:14.728Z",
    "name":"Paula Hodkiewicz",
    "details":{
        "price":"139.00",
        "description":"The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
        "color":"salmon"
    },
    "stock":1609,
    "id":"53"
}
fake_legacy_product_26 = {
    "createdAt":"2023-08-27T22:55:14.728Z",
    "name":"Titi",
    "details":{
        "price":"39.00",
        "description":"Un incroyable produit",
        "color":"purple"
    },
    "stock":2464,
    "id":"26"
}

fake_legacy_products = [
    fake_legacy_product_3,
    fake_legacy_product_53,
    fake_legacy_product_26
]

class TestERP:

    def test_get_customers(self, mocker):

        crm_util = CRMUtil()
        # erp_util.current_API = mocker.MagicMock()
        # erp_util.current_API.get_products.return_value = fake_legacy_products
        # stocks = erp_util.get_stocks()

        # expected_stocks = [
        #     {
        #         "value": 1609,
        #         "product_id": "53",
        #         "product_name": "Paula Hodkiewicz"
        #     },
        #     {
        #         "value": 2464,
        #         "product_id": "26",
        #         "product_name": "Titi"
        #     },
        #     {
        #         "value": 73254,
        #         "product_id": "3",
        #         "product_name": "Rufus Pacocha"
        #     }
        # ]


        customers = crm_util.get_customers()
        assert customers == {"toto": "titi"}