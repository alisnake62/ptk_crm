from util.crm import CRMUtil


fake_legacy_customer_7 = {
    "createdAt":"2023-08-29T17:41:41.077Z",
    "name":"Eugene Pfannerstill",
    "username":"Kyle_Sawayn66",
    "firstName":"Dahlia",
    "lastName":"Jaskolski",
    "address":{
        "postalCode":"51160",
        "city":"Phoenix"
    },
    "profile":{
        "firstName":"Vidal",
        "lastName":"Kuhic"
    },
    "company":{
        "companyName":"Harber - Steuber"
    },
    "id":"7",
    "orders":[
        {
            "createdAt":"2023-08-30T10:54:50.688Z",
            "id":"1",
            "customerId":"7"
        },
        {
            "createdAt":"2023-08-29T17:17:39.378Z",
            "id":"51",
            "customerId":"7"
        }
    ]
}
fake_legacy_customer_12 = {
    "createdAt":"2023-08-30T17:41:41.077Z",
    "name":"Martin Dupont",
    "username":"martinmatin",
    "firstName":"Martin",
    "lastName":"Dupont",
    "address":{
        "postalCode":"31400",
        "city":"Toulouse"
    },
    "profile":{
        "firstName":"Martin",
        "lastName":"Dupont"
    },
    "company":{
        "companyName":"Rubik's Cube Corporacy"
    },
    "id":"12",
    "orders":[]
}

fake_legacy_order_1 = {
    "createdAt":"2023-08-30T10:54:50.688Z",
    "id":"1",
    "customerId":"7",
    "products":[
        {
            "createdAt":"2023-08-30T08:29:52.728Z",
            "name":"Dorothy Dietrich",
            "details":{
                "price":"547.00",
                "description":"Boston's most advanced compression wear technology increases muscle oxygenation, stabilizes active muscles","color":"orchid"
            },
            "stock":16996,
            "id":"1",
            "orderId":"1"
        },
        {
            "createdAt":"2023-08-29T23:21:54.828Z",
            "name":"Fred Murphy",
            "details":{
                "price":"923.00",
                "description":"The Football Is Good For Training And Recreational Purposes","color":"lavender"
            },"stock":46781,
            "id":"51",
            "orderId":"1"
        }
    ]
}
fake_legacy_order_51 = {
    "createdAt":"2023-08-29T17:17:39.378Z",
    "id":"51",
    "customerId":"7",
    "products":[
        {
            "createdAt":"2023-08-30T08:29:52.728Z",
            "name":"Dorothy Dietrich",
            "details":{
                "price":"547.00",
                "description":"Boston's most advanced compression wear technology increases muscle oxygenation, stabilizes active muscles","color":"orchid"
            },
            "stock":16996,
            "id":"1",
            "orderId":"1"
        }
    ]
}


fake_legacy_customers = [
    fake_legacy_customer_12,
    fake_legacy_customer_7
]

fake_legacy_orders = [
    fake_legacy_order_1,
    fake_legacy_order_51
]

class TestERP:

    def test_get_customers(self, mocker):

        crm_util = CRMUtil()
        crm_util.current_API = mocker.MagicMock()
        crm_util.current_API.get_customers.return_value = fake_legacy_customers
        crm_util.current_API.get_orders.side_effect=[[], fake_legacy_orders]

        customers = crm_util.get_customers()

        expected_customers =  [
            {
                "createdAt":"2023-08-30T17:41:41.077Z",
                "name":"Martin Dupont",
                "username":"martinmatin",
                "firstName":"Martin",
                "lastName":"Dupont",
                "address":{
                    "postalCode":"31400",
                    "city":"Toulouse"
                },
                "profile":{
                    "firstName":"Martin",
                    "lastName":"Dupont"
                },
                "company":{
                    "companyName":"Rubik's Cube Corporacy"
                },
                "id":"12",
                "orders":[],
                "products_ordered": 0,
                "revenue": 0
            },
            {
                "createdAt":"2023-08-29T17:41:41.077Z",
                "name":"Eugene Pfannerstill",
                "username":"Kyle_Sawayn66",
                "firstName":"Dahlia",
                "lastName":"Jaskolski",
                "address":{
                    "postalCode":"51160",
                    "city":"Phoenix"
                },
                "profile":{
                    "firstName":"Vidal",
                    "lastName":"Kuhic"
                },
                "company":{
                    "companyName":"Harber - Steuber"
                },
                "id":"7",
                "orders":[
                    {
                        "createdAt":"2023-08-30T10:54:50.688Z",
                        "id":"1",
                        "customerId":"7"
                    },
                    {
                        "createdAt":"2023-08-29T17:17:39.378Z",
                        "id":"51",
                        "customerId":"7"
                    }
                ],
                "products_ordered": 3,
                "revenue": 2017.0
            }
        ]

        assert customers == expected_customers

    def test_get_customers_sorted_by_product_volume(self, mocker):

        crm_util = CRMUtil()
        crm_util.current_API = mocker.MagicMock()
        crm_util.current_API.get_customers.return_value = fake_legacy_customers
        crm_util.current_API.get_orders.side_effect=[[], fake_legacy_orders]

        customers = crm_util.get_customers(sorted_by="product_volume")

        expected_customers =  [
            {
                "createdAt":"2023-08-29T17:41:41.077Z",
                "name":"Eugene Pfannerstill",
                "username":"Kyle_Sawayn66",
                "firstName":"Dahlia",
                "lastName":"Jaskolski",
                "address":{
                    "postalCode":"51160",
                    "city":"Phoenix"
                },
                "profile":{
                    "firstName":"Vidal",
                    "lastName":"Kuhic"
                },
                "company":{
                    "companyName":"Harber - Steuber"
                },
                "id":"7",
                "orders":[
                    {
                        "createdAt":"2023-08-30T10:54:50.688Z",
                        "id":"1",
                        "customerId":"7"
                    },
                    {
                        "createdAt":"2023-08-29T17:17:39.378Z",
                        "id":"51",
                        "customerId":"7"
                    }
                ],
                "products_ordered": 3,
                "revenue": 2017.0
            },
            {
                "createdAt":"2023-08-30T17:41:41.077Z",
                "name":"Martin Dupont",
                "username":"martinmatin",
                "firstName":"Martin",
                "lastName":"Dupont",
                "address":{
                    "postalCode":"31400",
                    "city":"Toulouse"
                },
                "profile":{
                    "firstName":"Martin",
                    "lastName":"Dupont"
                },
                "company":{
                    "companyName":"Rubik's Cube Corporacy"
                },
                "id":"12",
                "orders":[],
                "products_ordered": 0,
                "revenue": 0
            },
        ]

        assert customers == expected_customers

    def test_get_customers_sorted_by_revenue_volume(self, mocker):

        crm_util = CRMUtil()
        crm_util.current_API = mocker.MagicMock()
        crm_util.current_API.get_customers.return_value = fake_legacy_customers
        crm_util.current_API.get_orders.side_effect=[[], fake_legacy_orders]

        customers = crm_util.get_customers(sorted_by="revenue_volume")

        expected_customers =  [
            {
                "createdAt":"2023-08-29T17:41:41.077Z",
                "name":"Eugene Pfannerstill",
                "username":"Kyle_Sawayn66",
                "firstName":"Dahlia",
                "lastName":"Jaskolski",
                "address":{
                    "postalCode":"51160",
                    "city":"Phoenix"
                },
                "profile":{
                    "firstName":"Vidal",
                    "lastName":"Kuhic"
                },
                "company":{
                    "companyName":"Harber - Steuber"
                },
                "id":"7",
                "orders":[
                    {
                        "createdAt":"2023-08-30T10:54:50.688Z",
                        "id":"1",
                        "customerId":"7"
                    },
                    {
                        "createdAt":"2023-08-29T17:17:39.378Z",
                        "id":"51",
                        "customerId":"7"
                    }
                ],
                "products_ordered": 3,
                "revenue": 2017.0
            },
            {
                "createdAt":"2023-08-30T17:41:41.077Z",
                "name":"Martin Dupont",
                "username":"martinmatin",
                "firstName":"Martin",
                "lastName":"Dupont",
                "address":{
                    "postalCode":"31400",
                    "city":"Toulouse"
                },
                "profile":{
                    "firstName":"Martin",
                    "lastName":"Dupont"
                },
                "company":{
                    "companyName":"Rubik's Cube Corporacy"
                },
                "id":"12",
                "orders":[],
                "products_ordered": 0,
                "revenue": 0
            },
        ]

        assert customers == expected_customers

    def test_get_customer(self, mocker):

        crm_util = CRMUtil()
        crm_util.current_API = mocker.MagicMock()
        crm_util.current_API.get_customer.return_value = fake_legacy_customer_7
        crm_util.current_API.get_orders.return_value = fake_legacy_orders

        customer = crm_util.get_customer(customer_id="7")

        expected_customer =  {
            "createdAt":"2023-08-29T17:41:41.077Z",
            "name":"Eugene Pfannerstill",
            "username":"Kyle_Sawayn66",
            "firstName":"Dahlia",
            "lastName":"Jaskolski",
            "address":{
                "postalCode":"51160",
                "city":"Phoenix"
            },
            "profile":{
                "firstName":"Vidal",
                "lastName":"Kuhic"
            },
            "company":{
                "companyName":"Harber - Steuber"
            },
            "id":"7",
            "orders":[
                {
                    "createdAt":"2023-08-30T10:54:50.688Z",
                    "id":"1",
                    "customerId":"7"
                },
                {
                    "createdAt":"2023-08-29T17:17:39.378Z",
                    "id":"51",
                    "customerId":"7"
                }
            ],
            "products_ordered": 3,
            "revenue": 2017.0,
            "toto": "titi"
        }

        assert customer == expected_customer