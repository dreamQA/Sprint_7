from enum import unique

import requests
import allure
import pytest
from data import TestData
from helpers import *
from urls import Urls
from http import HTTPStatus

class TestCreateCourier:

    @allure.title('Тест создания курьера')
    @allure.description('Проверка создания курьера')
    def test_create_courier_account_created(self,create_courier):
        courier_id = create_courier
        assert courier_id is not None


    @allure.title('Неуспешное создание курьера с повторно введенными данными')
    def test_create_duplicate_courier(self):
        courier_payload = register_new_courier_with_static_data()
        requests.post(Urls.URL_CREATE_COURIER,data = courier_payload)
        second_response= requests.post(Urls.URL_CREATE_COURIER,data = courier_payload)
        assert (second_response.status_code == HTTPStatus.CONFLICT and second_response.json() == TestData.MESSAGE_CONFLICT)

    @allure.title('Тест создания курьера с одним незаполненным полем,ожидаемый результат 400 BAD REQUEST')
    @pytest.mark.parametrize('fields', [
        {'login': '', 'password': generate_password(), 'firstName': generate_password()},
        {'login': generate_login(), 'password': '', 'firstName': generate_login()},
        {'login': generate_login(), 'password': generate_password(), 'firstName': ''},
    ])

    def test_create_courier_with_empty_fields(self, fields):
        response = requests.post(Urls.URL_CREATE_COURIER,data = fields)
        assert (response.status_code == HTTPStatus.BAD_REQUEST and response.json() == TestData.MESSAGE_BAD_REQUEST)

