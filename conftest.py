import pytest
import requests
from http import HTTPStatus
from urls import Urls
from helpers import *

@pytest.fixture(scope='function')
def create_courier():
    courier_payload = register_new_courier_and_return_login_password()
    response = requests.post(Urls.URL_CREATE_COURIER, data=courier_payload)
    assert response.status_code == HTTPStatus.CREATED and response.json() == {'ok': True}

    auth_response = requests.post(Urls.URL_LOGIN_COURIER, data={
        "login": courier_payload['login'],
        "password": courier_payload['password']
    })
    assert auth_response.status_code == HTTPStatus.OK

    courier_id = auth_response.json().get('id')
    assert courier_id is not None, "ID курьера не равно None после авторизации"

    yield courier_id

   # удаляем курьера после теста
    delete_response = requests.delete(Urls.URL_DELETE_COURIER.replace(':id',str(courier_id)))
    assert delete_response.status_code == HTTPStatus.OK and delete_response.json() == {'ok': True}



