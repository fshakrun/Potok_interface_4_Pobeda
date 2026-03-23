import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Tabs")
def test_tabs_switch(driver):
    with allure.step("Открыть страницу"):
        page = FlowPage(driver)
        page.open(BASE_URL)
        page.wait_page_loaded()

    with allure.step("Получить вкладки"):
        tabs = page.get_tabs()

    with allure.step("Проверить наличие вкладок"):
        assert tabs is not None
