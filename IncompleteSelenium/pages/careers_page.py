from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    LOCATIONS_SECTION = (By.CLASS_NAME, "col-12 col-md-6")
    TEAMS_SECTION = (By.CLASS_NAME, "col-12 d-flex flex-wrap p-0 career-load-more")
    LIFE_AT_SECTION = (By.CLASS_NAME, "elementor-section elementor-top-section elementor-element elementor-element-a8e7b90 elementor-section-full_width elementor-section-height-default elementor-section-height-default")

    QA_JOBS_BUTTON = (By.LINK_TEXT, "See all QA jobs")

    def is_careers_page_opened(self):
        return "Careers" in self.driver.title

    def are_sections_visible(self):
        return (self.is_element_visible(self.LOCATIONS_SECTION) and
                self.is_element_visible(self.TEAMS_SECTION) and
                self.is_element_visible(self.LIFE_AT_SECTION))

    def go_to_qa_jobs(self):
        self.driver.find_element(*self.QA_JOBS_BUTTON).click()
