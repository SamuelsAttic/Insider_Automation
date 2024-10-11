from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class JobsPage(BasePage):
    LOCATION_FILTER = (By.XPATH, f"//form[@id='top-filter-form']/div/span/span/span/span[2]/b") 
    DEPARTMENT_FILTER = (By.XPATH, f"//form[@id='top-filter-form']/div[2]/span/span/span/span[2]/b")
    JOB_LIST = (By.CLASS_NAME, "position-list-item")
    QA_JOBS_BUTTON = (By.CLASS_NAME, "btn.btn-outline-secondary.rounded.text-medium.mt-2.py-3.px-lg-5.w-100.w-md-50")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))).click()

        time.sleep(20)
        
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.LOCATION_FILTER)).click().perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*='Istanbul, Turkey']"))).click()
        actions.move_to_element(self.driver.find_element(*self.DEPARTMENT_FILTER)).click().perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*='Quality Assurance']"))).click()

    def are_jobs_present(self):
        return len(self.driver.find_elements(*self.JOB_LIST)) > 0

    def validate_jobs(self, location, department):
        jobs = self.driver.find_elements(*self.JOB_LIST)
        for job in jobs:
            job_location = job.find_element(By.CSS_SELECTOR, "[class*='position-location']").text
            job_department = job.find_element(By.CSS_SELECTOR, "[class*='position-department']").text
            job_position = job.find_element(By.CSS_SELECTOR, "[class*='position-title']").text
            if location not in job_location or department not in job_department or department not in job_position:
                return False
        return True

    def view_first_job_role(self):
        currentElement = self.driver.find_elements(*self.JOB_LIST)[0]
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((currentElement.find_element(By.CLASS_NAME, "btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5")))).click()

    def go_to_qa_jobs(self):
        self.driver.find_element(*self.QA_JOBS_BUTTON).click()
