import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Видимость элемента")
def test_items_visible(driver):
    page = FlowPage(driver)
    page.open(BASE_URL)
    page.wait_page_loaded()

    page.click_comments_tab()

    items = page.get_items()

    assert items is not None
