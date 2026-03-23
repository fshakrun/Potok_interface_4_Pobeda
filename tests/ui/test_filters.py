import allure
from utils.config import BASE_URL


@allure.title("Фильтрация по платформе")
@allure.description("Проверка, что пользователь может нажать на фильтр ВКонтакте")
def test_filter_buttons(driver):
    with allure.step("Открываем страницу"):
        driver.get(BASE_URL)

    with allure.step("Находим кнопку фильтра ВКонтакте"):
        vk_button = driver.find_element("xpath", "//button[contains(text(),'ВКонтакте')]")

    with allure.step("Кликаем по кнопке"):
        vk_button.click()

    with allure.step("Проверяем, что кнопка доступна"):
        assert vk_button.is_enabled()