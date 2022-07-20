from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.one_item_page import OneItem
import time


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price = (By.XPATH, "//div[contains(@class,'right-side')]//div[3]//div[3]//div[1]//div[1]//span[1]")
    link = (By.LINK_TEXT, "Stacionarus kompiuteris Hyrican Striker PCK06800 [Ryzen 7 5800X / 32GB RAM / 1TB SSD / RTX 3080 Ti / B550 / Win11]")

    def getting_price(self):
        time.sleep(2)
        self.wait_fo(self.price)
        return self.get_text(self.price)

    def press_link(self):
        self.click(self.link)
        one_item_page = OneItem(self.driver)
        return one_item_page
