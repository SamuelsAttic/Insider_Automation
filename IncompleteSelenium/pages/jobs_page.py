from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JobsPage(BasePage):
    LOCATION_FILTER = (By.ID, "filter-by-location")
    DEPARTMENT_FILTER = (By.ID, "filter-by-department")
    JOB_LIST = (By.CLASS_NAME, "position-list-item")
    QA_JOBS_BUTTON = (By.CLASS_NAME, "btn.btn-outline-secondary.rounded.text-medium.mt-2.py-3.px-lg-5.w-100.w-md-50")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
        self.driver.find_element(*self.LOCATION_FILTER).click()
        self.driver.find_element(By.XPATH, f"//span[text()='{location}']").click()

        self.driver.find_element(*self.DEPARTMENT_FILTER).click()
        self.driver.find_element(By.XPATH, f"//span[text()='{department}']").click()

    def are_jobs_present(self):
        return len(self.driver.find_elements(*self.JOB_LIST)) > 0

    def validate_jobs(self, location, department):
        jobs = self.driver.find_elements(*self.JOB_LIST)
        for job in jobs:
            job_location = job.find_element(By.CLASS_NAME, "location").text
            job_department = job.find_element(By.CLASS_NAME, "department").text
            job_position = job.find_element(By.CLASS_NAME, "title").text
            if location not in job_location or department not in job_department or department not in job_position:
                return False
        return True

    def view_first_job_role(self):
        self.driver.find_elements(*self.JOB_LIST)[0].find_element(By.LINK_TEXT, "View Role").click()

    def go_to_qa_jobs(self):
        self.driver.find_element(*self.QA_JOBS_BUTTON).click()
