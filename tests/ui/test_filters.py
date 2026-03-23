import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Фильтры")
def test_filter_buttons(driver):
    page = FlowPage(driver)
    page.open(BASE_URL)
    page.wait_page_loaded()

    buttons = page.get_buttons()

    # проверяем что кнопки вообще есть
    assert len(buttons) > 0
