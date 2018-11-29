from selenium import webdriver

from lesson10.pages.main_page import MainPage
from lesson10.pages.product_page import ProductPage
from lesson10.pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_to_cart(self, items):
        self.main_page.open()
        i = 1
        while i <= items:
            self.main_page.click_to_product(i)
            self.product_page.add_product_to_cart()
            self.product_page.wait_add_to_cart(i)
            self.product_page.click_to_logotype()
            i += 1

    def delete_from_cart(self):
        self.product_page.click_to_cart()

        i = 1
        count_products = self.cart_page.find_count_products()
        while i <= count_products:
            self.cart_page.get_product_in_table()
            self.cart_page.remove_product()
            self.cart_page.wait_delete_from_table()
            i += 1
