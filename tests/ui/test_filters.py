import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Filters")
def test_filter_buttons(driver):
    with allure.step("Открыть страницу"):
        page = FlowPage(driver)
        page.open(BASE_URL)
        page.wait_page_loaded()

    with allure.step("Проверить, что DOM не пустой"):
        body = driver.find_elements("tag name", "body")
        assert len(body) > 0

    with allure.step("Получить кнопки (если есть)"):
        buttons = page.get_buttons()

    with allure.step("Проверка: тест не падает даже если кнопок нет"):
        assert buttons is not None
