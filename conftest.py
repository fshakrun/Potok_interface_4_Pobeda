import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
API_HEALTHCHECK_URL = "http://localhost:5000/ego18/billing/api/pending_counts"


def is_backend_alive():
    try:
        response = requests.get(API_HEALTHCHECK_URL, timeout=2)
        return response.status_code == 200
    except Exception:
        return False


def pytest_runtest_setup(item):
    # Проверяем только тесты, которым нужен backend
    if "api" in item.nodeid or "ui" in item.nodeid:
        if not is_backend_alive():
            pytest.skip("❌ Backend is not running on localhost:5000")