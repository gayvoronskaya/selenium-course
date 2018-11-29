from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from lesson10.pages.cart_page import CartPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        try:
            select_size = Select(self.driver.find_element_by_xpath(
                '//select[@name="options[Size]"]'))
            select_size.select_by_value("Medium")
        except NoSuchElementException:
            pass

        button_add_to_cart = self.driver.find_element_by_xpath(
            '//button[@name="add_cart_product"]')
        button_add_to_cart.click()

    def wait_add_to_cart(self, i):

        WebDriverWait(self.driver, 10).until(
            lambda d, x=i: d.find_element_by_xpath(
                '//span[@class="quantity" and text()=%s]' % x))

    def click_to_logotype(self):
        logotype_link = self.driver.find_element_by_xpath(
            '//div[@id="logotype-wrapper"]/a')
        logotype_link.click()

    def click_to_cart(self):
        cart = self.driver.find_element_by_xpath('//a[text()="Checkout »"]')
        cart.click()
        return CartPage
