import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Фильтры")
def test_filter_buttons(driver):
    driver.get(BASE_URL)

    tabs = driver.find_elements(By.TAG_NAME, "button")

    assert len(tabs) > 0
