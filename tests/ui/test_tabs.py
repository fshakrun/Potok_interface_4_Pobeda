import allure
from utils.config import BASE_URL


@allure.title("Переключение вкладок")
@allure.description("Проверка, что пользователь может открыть вкладку комментариев")
def test_tabs_switch(driver):
    with allure.step("Открываем страницу"):
        driver.get(BASE_URL)

    with allure.step("Находим вкладку комментариев"):
        tab = driver.find_element("id", "comments-tab")

    with allure.step("Кликаем на вкладку"):
        tab.click()

    with allure.step("Проверяем, что вкладка отображается"):
        assert tab.is_displayed()