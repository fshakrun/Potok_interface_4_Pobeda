import allure
from selenium.webdriver.common.by import By
from utils.config import BASE_URL


@allure.feature("UI")
def test_search(driver):
    page = FlowPage(driver)
    page.open(BASE_URL)
    page.wait_page_loaded()

    page.click_comments_tab()
    page.open_search()
    page.search("тест")

    assert True 
