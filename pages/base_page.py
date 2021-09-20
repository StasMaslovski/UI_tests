from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def click_on_the_btn(self, how, what):
        self.browser.find_element(how, what).click()

    def get_value(self, how, what):
        return self.browser.find_element(how, what).text

    def comparing_values(self, value1, value2):
        assert value1 == value2, 'values is not equal'

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
