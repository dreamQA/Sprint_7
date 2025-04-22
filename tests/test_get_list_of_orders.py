import requests
import pytest
import allure
from http import HTTPStatus
from urls import Urls

class TestGetListOfOrders:
    @allure.title('Проверка успешного получения списка заказа')
    def test_get_orders_list(self):
        response = requests.get(Urls.URL_GET_ORDERS_LIST)
        assert (response.status_code == HTTPStatus.OK and 'orders' in response.text)