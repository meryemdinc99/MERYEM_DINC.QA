from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers')]")

    def open_home(self):
        self.visit("https://useinsider.com/")

    def go_to_careers(self):
        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)
