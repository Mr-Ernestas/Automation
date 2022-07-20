from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time

class OneItem(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price = (By.XPATH, "//div[@class='right-side deviating-height ']//div[@class='pricing-left no-discount']//span[1]")
    cart_button = (By.XPATH, "(//a[@class='primary-button full-width add-to-cart in-stock'])[1]")
    car_page_button = (By.XPATH, "//span[contains(text(),'Krepšelis')]")
    buy = (By.XPATH, "//button[@class='primary-button']")

    def getting_price(self):
        self.wait_fo(self.price)
        return self.get_text(self.price)

    def press_button(self):
        self.click(self.cart_button)

    def press_cart(self):
        self.click(self.car_page_button)

    def press_buy(self):
        self.click(self.buy)
