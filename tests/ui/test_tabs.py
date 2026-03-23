import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Переключение вкладок")
def test_tabs_switch(driver):
    page = FlowPage(driver)
    page.open(BASE_URL)
    page.wait_page_loaded()

    tabs = page.get_tabs()

    # проверяем наличие элементов интерфейса
    assert tabs is not None
