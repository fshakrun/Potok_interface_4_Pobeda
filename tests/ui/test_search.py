import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Поиск")
def test_search(driver):
  driver.get(BASE_URL)

    inputs = driver.find_elements(By.TAG_NAME, "input")

    assert inputs is not None
