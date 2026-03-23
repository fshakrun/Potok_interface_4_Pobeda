from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlowPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

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
            # fallback — если нет id
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                self.driver.execute_script("arguments[0].click();", buttons[0])

    def get_items(self):
        return self.driver.find_elements(By.XPATH, "//div")

    def open_search(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        if buttons:
            self.driver.execute_script("arguments[0].click();", buttons[0])

    def search(self, text):
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        if inputs:
            inputs[0].clear()
            inputs[0].send_keys(text)
