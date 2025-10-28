from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class QaJobsPage(BasePage):
    SEE_ALL_JOBS = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    FILTER_LOC = (By.XPATH, "//span[contains(text(), 'Istanbul, Turkey')]")
    FILTER_DEPT = (By.XPATH, "//span[contains(text(), 'Quality Assurance')]")
    JOB_LIST = (By.CSS_SELECTOR, "div.position-list div.position-title")
    VIEW_ROLE_BTN = (By.XPATH, "//a[contains(text(), 'View Role')]")

    def open_all_jobs(self):
        self.click(self.SEE_ALL_JOBS)
        time.sleep(2)

    def filter_jobs(self):
        self.click(self.FILTER_LOC)
        self.click(self.FILTER_DEPT)
        time.sleep(2)

    def verify_job_list(self):
        jobs = self.driver.find_elements(*self.JOB_LIST)
        assert len(jobs) > 0, "No job listed"
        for job in jobs:
            text = job.text.lower()
            assert "quality assurance" in text, f"Unexpected job: {text}"

    def click_view_role(self):
        self.click(self.VIEW_ROLE_BTN)
