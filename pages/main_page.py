from selenium.webdriver.common.by import By
from pages.menu_page import MenuPage
from pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    main_computer = (By.XPATH, "//a[@title='Kompiuterinė technika']")
    main_registration = (By.XPATH, "//div[@class='reg-login']//a")

    def getting_text(self):
        self.wait_fo(self.main_registration)
        return self.get_text(self.main_registration)

    def go_next_page(self):
        self.click(self.main_computer)
        menu_page = MenuPage(self.driver)
        return menu_page

