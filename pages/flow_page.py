from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlowPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

        # Ждём полной загрузки HTML
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def click_comments_tab(self):
        tab = self.wait.until(
            EC.element_to_be_clickable((By.ID, "comments-tab"))
        )

        # JS click стабильнее в CI
        self.driver.execute_script("arguments[0].click();", tab)

        # ждём, что что-то появилось после клика
        self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )

    def open_search(self):
        search_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Поиск')]"))
        )
        search_btn.click()

    def search(self, text):
        input_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input"))
        )
        input_field.clear()
        input_field.send_keys(text)

    def get_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div"))
        )
