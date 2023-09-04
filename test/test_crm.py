from util.crm import CRMUtil


fake_legacy_customer_1 = {
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
fake_legacy_customer_2 = {
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
    "orders":[
        {
            "createdAt":"2023-08-31T10:54:50.688Z",
            "id":"11",
            "customerId":"12"
        },
        {
            "createdAt":"2023-08-30T17:17:39.378Z",
            "id":"151",
            "customerId":"12"
        }
    ]
}


fake_legacy_customer = [
    fake_legacy_customer_1,
    fake_legacy_customer_2
]

class TestERP:

    def test_get_customers(self, mocker):

        crm_util = CRMUtil()
        crm_util.current_API = mocker.MagicMock()
        crm_util.current_API.get_customers.return_value = fake_legacy_customer

        customers = crm_util.get_customers()
        assert customers == fake_legacy_customer