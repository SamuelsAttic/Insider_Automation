from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage
import pytest

def test_insider_careers(get_driver):
    driver = get_driver
    home_page = HomePage(driver)
    
    # Step 1: Visit home page and check if opened
    assert home_page.is_home_page_opened(), "Home page did not open"
    
    # Step 2: Navigate to Careers and check if sections are visible
    home_page.navigate_to_careers()
    careers_page = CareersPage(driver)
    assert careers_page.is_careers_page_opened(), "Careers page did not open"
    assert careers_page.are_sections_visible(), "Not all sections are visible on Careers page"
    
    # Step 3: Go to QA jobs, filter, and check jobs
    careers_page.go_to_qa_jobs()
    jobs_page = JobsPage(driver)
    jobs_page.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
    assert jobs_page.are_jobs_present(), "No jobs present after filtering"
    
    # Step 4: Validate all jobs contain the correct department and location
    assert jobs_page.validate_jobs(location="Istanbul, Turkey", department="Quality Assurance"), "Job validation failed"

    # Step 5: View role and verify redirection to Lever Application form
    jobs_page.view_first_job_role()
    assert "lever.co" in driver.current_url, "Failed to redirect to Lever Application form"
