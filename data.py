class TestData:
    CORRECT_LOGIN = "DreamQA"
    CORRECT_PASSWORD = "123456"
    CORRECT_NAME = "Alexander"

    ORDER_DATA = {
        "first_name": "Alexander",
        "last_name": "Gaidai",
        "address1": "Lenina 102",
        "metroStation": 4,
        "phone": "+8 982 467 43 64",
        "realTime" : 5,
        "deliveryDate": "2025-04-25",
        "comment": "dont call"
    }

    MESSAGE_CONFLICT = {"code": 409,"message":"Этот логин уже используется. Попробуйте другой."}
    MESSAGE_BAD_REQUEST = {'code': 400,"message":"Недостаточно данных для создания учетной записи"}
    MESSAGE_LOGIN_BAD_REQUEST = {'code': 400, 'message': 'Недостаточно данных для входа'}
    MESSAGE_NOT_FOUND = {'code': 404,"message":"Учетная запись не найдена"}