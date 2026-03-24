import requests
import allure
from utils.config import API_BASE


@allure.feature("API")
@allure.story("Доступность API")
@allure.title("Проверка доступности API")
@allure.description("Проверка, что API отвечает и доступен")
def test_api_is_alive():
    with allure.step("Отправляем GET запрос к pending_counts"):
        response = requests.get(f"{API_BASE}/ego18/billing/api/pending_counts")

    with allure.step("Проверяем статус код 200"):
        assert response.status_code == 200


@allure.feature("API")
@allure.story("Счетчики комментариев")
@allure.title("Проверка счетчиков комментариев")
@allure.description("API должен возвращать корректное количество элементов")
def test_pending_counts():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(f"{API_BASE}/ego18/billing/api/pending_counts")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем структуру ответа"):
        data = response.json()
        assert isinstance(data, dict)
        assert "all_count" in data

    with allure.step("Проверяем значение счетчика"):
        assert data["all_count"] >= 0


@allure.feature("API")
@allure.story("Фильтры")
@allure.title("Проверка фильтров")
@allure.description("API должен возвращать фильтры comments и reviews")
def test_filter_counts():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(f"{API_BASE}/ego18/billing/api/filter_counts")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем структуру ответа"):
        data = response.json()
        assert isinstance(data, dict)
        assert "comments" in data
        assert "reviews" in data


@allure.feature("API")
@allure.story("Управление ботом")
@allure.title("Остановка бота")
@allure.description("Проверка, что API корректно останавливает бота")
def test_stop_bot():
    with allure.step("Отправляем запрос на остановку бота"):
        response = requests.get(f"{API_BASE}/ego18/cloner/stop/clone_18/bot")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем ответ API"):
        data = response.json()
        assert data["success"] is True


@allure.feature("API")
@allure.story("Управление ботом")
@allure.title("Запуск бота")
@allure.description("Проверка, что API корректно запускает бота")
def test_start_bot():
    with allure.step("Отправляем запрос на запуск бота"):
        response = requests.get(f"{API_BASE}/ego18/cloner/start/clone_18/bot")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем ответ API"):
        data = response.json()
        assert data["success"] is True
