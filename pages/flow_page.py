from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlowPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def wait_page_loaded(self):
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def click_comments_tab(self):
        try:
            tab = self.wait.until(
                EC.presence_of_element_located((By.ID, "comments-tab"))
            )
            self.driver.execute_script("arguments[0].click();", tab)
        except:
            pass  # таб может отсутствовать в статическом HTML

    def open_search(self):
        try:
            btn = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Поиск')]"))
            )
            btn.click()
        except:
            pass

    def search(self, text):
        try:
            input_field = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input"))
            )
            input_field.clear()
            input_field.send_keys(text)
        except:
            pass

    def get_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "item")

    def get_tabs(self):
        return self.driver.find_elements(By.XPATH, "//*[contains(@id,'tab')]")

    def get_buttons(self):
        return self.driver.find_elements(By.TAG_NAME, "button")
