from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.product_page import ProductPage
from selenium.webdriver.common.keys import Keys



class ComputersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cookies = (By.XPATH, "//a[@id='c-right']")
    text = (By.XPATH, "//div[@class='for-desktop']//ul")
    search_bar = (By.XPATH, "(//input[@placeholder='Ieškoti'])[2]")
    video_card = (By.XPATH, "//span[normalize-space()='GeForce RTX 3080Ti']")

    def clicking_cookies(self):
        self.click(self.cookies)

    def getting_text(self):
        self.wait_fo(self.text)
        return self.get_text(self.text)

    def searching(self, name):
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        self.send_keys(self.search_bar, name)

    def going_to_next_page(self):
        self.click(self.video_card)
        product_page = ProductPage(self.driver)
        return product_page
