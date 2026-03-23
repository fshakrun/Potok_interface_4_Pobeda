import allure
from pages.flow_page import FlowPage
from utils.config import BASE_URL


@allure.title("Отображение списка комментариев")
@allure.description("Проверка, что список комментариев загружается")
def test_items_visible(driver):
    page = FlowPage(driver)

    with allure.step("Открываем страницу"):
        page.open(BASE_URL)

    with allure.step("Переходим во вкладку комментариев"):
        page.click_comments_tab()

    with allure.step("Получаем элементы списка"):
        items = page.get_items()

    with allure.step("Проверяем, что список не пустой"):
        assert len(items) > 0