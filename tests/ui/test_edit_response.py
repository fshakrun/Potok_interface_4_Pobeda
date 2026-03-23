import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Видимость элемента")
def test_items_visible(driver):
    page = FlowPage(driver)

    with allure.step("Открыть страницу"):
        page.open(BASE_URL)

    with allure.step("Клик по вкладке комментов"):
        page.click_comments_tab()

    with allure.step("Проверка наличия элемента"):
        items = page.get_items()
        assert len(items) > 0
