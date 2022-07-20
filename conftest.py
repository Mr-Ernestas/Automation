import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from pages.computers_page import ComputersPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.one_item_page import OneItem
from pages.product_page import ProductPage


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\edovgial\Downloads\chromedriver.exe")

    driver.maximize_window()
    driver.get("https://www.varle.lt/")
    request.cls.mainPage = MainPage(driver)
    request.cls.menuPage = MenuPage(driver)
    request.cls.computersPage = ComputersPage(driver)
    request.cls.productPage = ProductPage(driver)
    request.cls.oneitemPage = OneItem(driver)
    yield
    # driver.close()