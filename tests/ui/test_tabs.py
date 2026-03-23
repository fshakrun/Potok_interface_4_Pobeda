import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Переключение вкладок")
def test_tabs_switch(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 15)

    tab = wait.until(
        EC.presence_of_element_located((By.ID, "comments-tab"))
    )

    driver.execute_script("arguments[0].click();", tab)

    assert tab is not None
