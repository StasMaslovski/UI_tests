import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    browser = webdriver.Chrome(C:\chromedriver)
    yield browser
    print("\nquit browser..")
    browser.quit()
