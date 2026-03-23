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

    with allure.step("Получить кнопки"):
        buttons = page.get_buttons()

    with allure.step("Проверить, что кнопки присутствуют"):
        assert len(buttons) > 0
