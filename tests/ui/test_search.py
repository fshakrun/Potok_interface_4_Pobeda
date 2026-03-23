import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Поиск")
def test_search(driver):
    page = FlowPage(driver)

    page.open(BASE_URL)
    page.click_comments_tab()

    with allure.step("Открыть поиск"):
        try:
            page.open_search()
        except:
            pass  # если кнопки нет — не падаем

    with allure.step("Осуществить поиск"):
        page.search("тест")

    with allure.step("Проверить результа"):
        items = page.get_items()
        assert len(items) > 0
