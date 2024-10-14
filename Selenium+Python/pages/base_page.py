from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator, timeout=10):
        try:
            element = self.wait_for_element(locator, timeout)
            return element.is_displayed()
        except:
            return False

    def take_screenshot(self, name="screenshot"):
        self.driver.save_screenshot(f"{name}.png")
