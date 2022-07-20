from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.computers_page import ComputersPage


class MenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    text = (By.XPATH, "//div[@class='for-desktop']//ul")
    menu_computer = (By.XPATH, "//a[@href='/stacionarus-kompiuteriai/']")

    def getting_text(self):
        self.wait_fo(self.text)
        return self.get_text(self.text)

    def go_next_page(self):
        self.click(self.menu_computer)
        computers_page = ComputersPage(self.driver)
        return computers_page
