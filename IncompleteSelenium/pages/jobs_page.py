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
        time.sleep(3)

    def are_jobs_present(self):
        return len(self.driver.find_elements(*self.JOB_LIST)) > 0

    def validate_jobs(self, location, department):
        jobs = self.driver.find_elements(*self.JOB_LIST)
        for job in jobs:
            job_location = job.find_element(By.CSS_SELECTOR, "[class*='position-location']").text
            job_department = job.find_element(By.CSS_SELECTOR, "[class*='position-department']").text
            job_position = job.find_element(By.CSS_SELECTOR, "[class*='position-title']").text
            print(f"Job location: {job_location}, Expected: {location}")
            print(f"Job department: {job_department}, Expected: {department}")
            print(f"Job department: {job_position}, Expected: {department}")

            if location not in job_location or department not in job_department or department not in job_position:
                return False
        return True

    def view_first_job_role(self):
        wait = WebDriverWait(self.driver, 15)
        currentElemnt = self.driver.find_elements(*self.JOB_LIST)[0].find_element(By.XPATH, f"//*[@id='jobs-list']/div/div/a")

        view_role_button = wait.until(EC.element_to_be_clickable((currentElemnt)))
        print(view_role_button.text)
        actions = ActionChains(self.driver)
        actions.move_to_element(view_role_button).perform()
        view_role_button.click()

        wait.until(EC.url_contains("https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc"))
        assert "lever.co" in self.driver.current_url, "Not redirected to Lever Application form page"

    def go_to_qa_jobs(self):
        self.driver.find_element(*self.QA_JOBS_BUTTON).click()
