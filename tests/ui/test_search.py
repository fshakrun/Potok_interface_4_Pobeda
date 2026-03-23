import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.feature("UI")
@allure.story("Search")
def test_search(driver):
    with allure.step("Открыть страницу"):
        page = FlowPage(driver)
        page.open(BASE_URL)
        page.wait_page_loaded()

    with allure.step("Открыть вкладку комментариев"):
        page.click_comments_tab()

    with allure.step("Открыть поиск"):
        page.open_search()

    with allure.step("Выполнить поиск"):
        page.search("тест")

    with allure.step("Проверка: тест не упал"):
        assert True
