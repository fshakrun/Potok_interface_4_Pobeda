from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlowPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click_first_edit(self):
        self.wait.until(
            lambda d: d.find_element("class name", "edit-btn")
        ).click()
        
    def click_comments_tab(self):
        tab = wait_for_element_clickable(self.driver, (By.ID, "comments-tab"))
        self.driver.execute_script("arguments[0].click();", tab)

    def open_search(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "toggleSearch"))).click()

    def search(self, text):
        input_el = self.wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        input_el.clear()
        input_el.send_keys(text)

    def get_items(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-group-item")))

    def toggle_bot(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "botToggle"))).click()
