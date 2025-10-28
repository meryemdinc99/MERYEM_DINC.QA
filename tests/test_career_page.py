from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QaJobsPage
from selenium.webdriver.support.ui import WebDriverWait


def test_insider_career_flow(driver):
    home = HomePage(driver)
    careers = CareersPage(driver)
    qa_page = QaJobsPage(driver)

    # 1️⃣ Home page
    home.open_home()
    assert "Insider" in home.get_title(), "Home page not opened"

    # 2️⃣ Careers page
    home.go_to_careers()
    WebDriverWait(driver, 20).until(lambda d: "careers" in d.current_url.lower())
    assert "careers" in driver.current_url.lower(), f"Careers page not opened. Current URL: {driver.current_url}"
    careers.verify_sections_visible()

    # 3️⃣ QA Jobs page
    careers.go_to_qa_page()
    assert "quality-assurance" in driver.current_url, "QA page not opened"
    qa_page.open_all_jobs()
    qa_page.filter_jobs()
    qa_page.verify_job_list()

    # 4️⃣ View Role
    qa_page.click_view_role()
    assert "lever.co" in driver.current_url, "Did not redirect to Lever application form"
