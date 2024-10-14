from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_MENU = (By.LINK_TEXT, "Careers")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com/")
    
    def is_home_page_opened(self):
        return "Insider" in self.driver.title

    def navigate_to_careers(self):
        # Wait for the 'Company' menu to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COMPANY_MENU)
        )
        self.driver.find_element(*self.COMPANY_MENU).click()

        # Wait for the 'Careers' menu option to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CAREERS_MENU)
        )
        self.driver.find_element(*self.CAREERS_MENU).click()