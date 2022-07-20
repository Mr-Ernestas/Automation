from test.base_test import BaseTest
import time


class TestE2E(BaseTest):

    def test_main_text(self):
        self.mainPage.getting_text()
        assert "Registracija" in self.mainPage.getting_text()

    def test_main_select(self):
        self.mainPage.go_next_page()

    def test_menu_text(self):
        self.menuPage.getting_text()
        assert "Kompiuterinė technika" in self.menuPage.getting_text()

    def test_menu(self):
        self.menuPage.go_next_page()

    def test_cookies(self):
        self.computersPage.clicking_cookies()

    def test_computers_text(self):
        self.computersPage.getting_text()
        assert "Stacionarūs kompiuteriai" in self.computersPage.getting_text()

    def test_search_cpu(self):
        self.computersPage.searching("RTX 3080ti")

    def test_going_next(self):
        self.computersPage.going_to_next_page()

    def test_price(self):
        self.productPage.getting_price()
        assert "2578" in self.productPage.getting_price()

    def test_press_link(self):
        self.productPage.press_link()

    def test_one_price(self):
        self.oneitemPage.getting_price()
        assert "2578" in self.oneitemPage.getting_price()

    def test_press_button(self):
        self.oneitemPage.press_button()

    def test_buy_button(self):
        self.oneitemPage.press_buy()

    def test_cart_button(self):
        self.oneitemPage.press_cart()






