import allure
from selenium.webdriver.common.by import By
from utils.config import BASE_URL


@allure.feature("UI")
def test_search(driver):
    driver.get(BASE_URL)

    inputs = driver.find_elements(By.TAG_NAME, "input")

    assert inputs is not None
