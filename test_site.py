import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser


def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html')
