import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.title("Поиск комментариев")
@allure.description("Проверка поиска по ключевому слову")
def test_search(driver):
    page = FlowPage(driver)

    with allure.step("Открываем страницу"):
        page.open(BASE_URL)

    with allure.step("Переходим во вкладку комментариев"):
        page.click_comments_tab()

    with allure.step("Открываем поиск"):
        page.open_search()

    with allure.step("Вводим поисковый запрос"):
        page.search("Негативный")

    with allure.step("Получаем список элементов"):
        items = page.get_items()

    with allure.step("Проверяем, что результаты найдены"):
        assert len(items) > 0