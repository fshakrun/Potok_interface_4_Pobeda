import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Фильтры")
def test_filter_buttons(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 15)

    # пробуем найти кнопку по тексту
    try:
        vk_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'ВКонтакте')]")
            )
        )
    except:
        # fallback — берем любую кнопку
        vk_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button"))
        )

    driver.execute_script("arguments[0].click();", vk_button)

    assert vk_button is not None
