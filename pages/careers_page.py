from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
import time

class CareersPage(BasePage):
    # Locators
    LOCATIONS = (By.XPATH, "//*[contains(text(), 'Our Locations')]")
    TEAMS = (By.XPATH, "//*[contains(text(), 'Find your calling')]")
    LIFE = (By.XPATH, "//*[contains(text(), 'Life at Insider')]")
    QA_PAGE = (By.XPATH, "//a[contains(@href, 'quality-assurance')]")

    def verify_sections_visible(self):
        # Wait for page load
        time.sleep(2)
        
        # Handle cookie consent if present
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_button.click()
        except:
            pass

        # Scroll down gradually
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        for height in range(0, total_height, 300):
            self.driver.execute_script(f"window.scrollTo(0, {height})")
            time.sleep(0.5)

        # Verify each section
        sections = [self.LOCATIONS, self.TEAMS, self.LIFE]
        for section in sections:
            try:
                element = self.wait.until(EC.presence_of_element_located(section))
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
                    element
                )
                time.sleep(1)
                assert element.is_displayed(), f"{section[1]} section not visible"
            except Exception as e:
                self.driver.save_screenshot(f"screenshots/section_error_{time.strftime('%Y%m%d_%H%M%S')}.png")
                raise AssertionError(f"Failed to verify {section[1]}: {str(e)}")

    def go_to_qa_page(self):
        try:
            qa_link = self.wait.until(EC.element_to_be_clickable(self.QA_PAGE))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", qa_link)
            time.sleep(1)
            qa_link.click()
        except Exception as e:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            self.driver.save_screenshot(f"screenshots/qa_page_error_{timestamp}.png")
            raise Exception(f"Failed to click QA page link: {str(e)}")
